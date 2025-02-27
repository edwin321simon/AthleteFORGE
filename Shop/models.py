from django.db import models
from Guest.models import *

# Create your models here.

class tbl_product(models.Model):
     product_name=models.CharField(max_length=20)
     product_price=models.CharField(max_length=20)
     shop=models.ForeignKey(tbl_shop,on_delete=models.CASCADE)
     scategory=models.ForeignKey(tbl_scategory,on_delete=models.CASCADE)
     product_photo=models.FileField(upload_to='ProductPhoto/')
     product_stock=models.IntegerField(default=0)
     product_discription=models.CharField(max_length=500)
     
class tbl_product_gallery(models.Model):
     product_image = models.FileField(upload_to='Product_Photos/')
     product = models.ForeignKey(tbl_product,on_delete=models.CASCADE)