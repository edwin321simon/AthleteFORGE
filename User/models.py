from django.db import models
from Guest.models import *
from Coach.models import *
from Shop.models import *

# Create your models here.

class tbl_booking(models.Model):
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     booking_date=models.DateField(auto_now_add=True)
     booking_deliverydate=models.DateField(null=True)
     booking_amount=models.CharField(max_length=20)
     booking_status=models.CharField(max_length=1,default="0",null=True)

class tbl_cart(models.Model):
     cart_quantity=models.CharField(max_length=10)
     product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
     booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
     cart_status=models.CharField(max_length=1,default="0",null=True)


class tbl_rating(models.Model):
    rating_data=models.IntegerField()
    user_name=models.CharField(max_length=500)
    user_review=models.CharField(max_length=500)
    coach=models.ForeignKey(tbl_coach,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(tbl_product,on_delete=models.SET_NULL,null=True)
    datetime=models.DateTimeField(auto_now_add=True)


class tbl_follow(models.Model):
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     coach=models.ForeignKey(tbl_coach,on_delete=models.CASCADE)


class tbl_checkbox(models.Model):
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     workout=models.ForeignKey(tbl_workout,on_delete=models.CASCADE)

class tbl_subscribe(models.Model):
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     subscription=models.ForeignKey(tbl_subscription,on_delete=models.CASCADE)
     status = models.IntegerField(default=0)


class tbl_wishlist(models.Model):
     user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
     product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)