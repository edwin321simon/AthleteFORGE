from django.shortcuts import render,redirect
from Admin.models import *
from Guest.models import *
from Coach.models import *
from User.models import *
from django.db.models import Q
from datetime import datetime
# Create your views here.

def CoachHP(request):
    coach = tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        return render(request,"Coach/CoachHP.html")
    else:
        return render(request,"Coach/CoachHP.html",{"data":coach})

def ViewCoach(request):
    coach = tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        return render(request,"Coach/Viewprofile.html"),
    else:
        return render(request,"Coach/Viewprofile.html",{"data": coach})
    
def EditCoach(request):
    coach=tbl_coach.objects.get(id=request.session["cid"])
    if request.method=="POST":
        coach.coach_name=request.POST.get("txt_name")
        coach.coach_contact=request.POST.get("txt_contact")
        coach.coach_address=request.POST.get("txt_address")
        coach.save()
        return redirect("webcoach:ViewCoach")
    else:
        return render(request,"Coach/EditProfile.html",{"data":coach})
    

def EPCoach(request):
    if request.method=="POST":
        coach=tbl_coach.objects.get(id=request.session['cid'])
        opassword=request.POST.get("txt_opassword")
        npassword=request.POST.get("txt_npassword")
        cpassword=request.POST.get("txt_cpassword")
        if coach.coach_password==opassword:
            if npassword == cpassword:
                coach.coach_password=request.POST.get("txt_npassword")
                coach.save()
                return redirect("webcoach:ViewCoach")
            else:
                msg="password missmatch !"
                return render(request,"Coach/Changepassword.html",{'msg':msg})
        else:
            msg="password missmatch !"
            return render(request,"Coach/Changepassword.html",{'msg':msg})
    else:
        return render(request,"Coach/Changepassword.html")



def Trainingdetails(request):
    event=tbl_event.objects.all()
    training=tbl_trainig.objects.all()
    if request.method == "POST":
        coach = tbl_coach.objects.get(id=request.session['cid'])
        event = coach.event_id
        eventdata = tbl_event.objects.get(id=event)
        tbl_trainig.objects.create(coach=coach,
                                 event = eventdata,
                                 training_duration=request.POST.get("txt_duration"),
                                 training_details=request.POST.get("txt_details"),
                                 
                                )   
        return redirect("webcoach:Trainingdetails")
    else:
        return render(request,"Coach/Trainingdetails.html",{"data":event,"tdata":training})  
    
def deletetraining_details(request,id):
    tbl_trainig.objects.get(id=id).delete()
    return redirect("webcoach:Trainingdetails")
    

def AddSubscription(request):
    subscription=tbl_subscription.objects.all()
    if request.method=="POST":
        tbl_subscription.objects.create(subscription_amount=request.POST.get("txt_amount"),
                                     subscription_details=request.POST.get("txt_details"),
                                     subscription_duration=request.POST.get("txt_duration"),
                                     coach=tbl_coach.objects.get(id=request.session["cid"])
                                     )
        return render(request,"Coach/Addsubscription.html",{"data":subscription})
    else:
        return render(request,"Coach/Addsubscription.html",{"data":subscription})
    

def DailyPlan(request,id):
    dailyplan=tbl_dailyplan.objects.filter(training=id)
    traning = tbl_trainig.objects.get(id=id)
    if request.method=="POST":
        dp = tbl_dailyplan.objects.filter(dailyplan_day=request.POST.get("txt_day")).count()
        if dp > 0:
            dpcount = tbl_dailyplan.objects.filter(training=id).count()
            if dpcount > int(traning.training_duration):
                return render(request,"Coach/DailyPlan.html",{"msg":"Count Exceed","id":id})
            else:
                return render(request,"Coach/DailyPlan.html",{"msg":"Date Is Repeated","id":id})
        else:
            dpcount = tbl_dailyplan.objects.filter(training=id).count()
            if dpcount >= int(traning.training_duration):
                return render(request,"Coach/DailyPlan.html",{"msg":"Count Exceed","id":id})
            else:
                training = tbl_trainig.objects.get(id=id)
                tbl_dailyplan.objects.create(training=training,
                                            dailyplan_day=request.POST.get("txt_day"),
                                            dailyplan_wcount=request.POST.get("txt_workout"),
                                            )
                return render(request,"Coach/DailyPlan.html",{"data":dailyplan})
    else:
        return render(request,"Coach/DailyPlan.html",{"data":dailyplan})
    



def Workout(request,id):
    workout=tbl_workout.objects.filter(dailyplan=id)
    workoutcount=tbl_workout.objects.filter(dailyplan=id).count()
    dite = tbl_dailyplan.objects.get(id=id)
    ditecount = dite.dailyplan_wcount
    if workoutcount >= int(ditecount):
        return render(request,"Coach/Workout.html",{"data":workout,"alt":1})
    else:
        if request.method=="POST":
            dailyplan=tbl_dailyplan.objects.get(id=id)
            tbl_workout.objects.create(dailyplan=dailyplan,
                                    workout_name=request.POST.get("txt_name"),
                                    workout_discription=request.POST.get("txt_description"),
                                    workout_file=request.FILES.get("txt_file"),
                                    )
            return render(request,"Coach/Workout.html",{"msg":"Data Added..","ID":id})
        else:
            return render(request,"Coach/Workout.html",{"data":workout})
        


def Followers(request):
    follower = tbl_follow.objects.filter(coach=request.session["cid"])
    return render(request,"Coach/Followers.html",{"data":follower})

def chatpage(request,id):
    foll = tbl_subscribe.objects.get(id=id)
    user  = tbl_user.objects.get(id=foll.user_id)
    # print(user.user_name)
    return render(request,"Coach/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_coach.objects.get(id=request.session["cid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),coach_from=from_user,user_to=to_user,chat_file=request.FILES.get("file"))
    return render(request,"Coach/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_coach.objects.get(id=request.session["cid"])
    chat_data = tbl_chat.objects.filter((Q(coach_from=user) | Q(coach_to=user)) & (Q(user_from=tid) | Q(user_to=tid))).order_by('chat_time')
    return render(request,"Coach/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(coach_from=request.session["cid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(coach_to=request.session["cid"]))).delete()
    return render(request,"Coach/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})


def Complaint(request):
    if request.method=="POST":
        Complaint= complaint.objects.create(coach=tbl_coach.objects.get(id=request.session["cid"]),complaint_title=request.POST.get("txt_title"),complaint_content=request.POST.get("txt_content"))
        return render(request,"Coach/Complaint.html")
    else:
        return render(request,"Coach/Complaint.html")
    


def Contact(request):
    if request.method == "POST":
        tbl_queries.objects.create(queries_name=request.POST.get("txt_name"),queries_email=request.POST.get("txt_email"),queries_message=request.POST.get("txt_message"))
        return redirect("webcoach:Contact")
    else:
        return render(request,'Coach/contact.html')
    

def About(request):
    return render(request,"Coach/about.html")

def viewcomplaints(request):
    if 'cid' in request.session:
        coach=tbl_coach.objects.all()
        coachcom=complaint.objects.filter(coach__in=coach)
        return render(request,"Coach/ViewComplaint.html",{'coach':coachcom})
    else:
        return redirect("webguest:Login")
    
def deleteSubscription(request,id):
    tbl_subscription.objects.get(id=id).delete()
    return redirect("webcoach:AddSubscription")

def viewsub(request):
    data = tbl_subscribe.objects.filter(subscription__coach=request.session["cid"])
    return render(request,"Coach/View_subscribes.html",{"data":data})

def Logout(request):
    del request.session["cid"]
    return redirect("webguest:Login")
