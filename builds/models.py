from django.db import models
from django.utils import timezone
import datetime
from django.conf import settings
import json

# Create your models here.
class Buildorders(models.Model):
    writer= models.CharField(max_length=30,verbose_name='Yazar')
    username=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,verbose_name='Kullanıcı Adı')
    headline= models.CharField(max_length=40,verbose_name='Başlık')
    buildorder= models.TextField(verbose_name='Build Order',default=" ",blank=bool)
    pub_date= models.DateTimeField(auto_now= True,verbose_name='Yayınlanma Tarihi')
    explanation=models.CharField(max_length=100,verbose_name='Açıklama')
    age=models.CharField(max_length=40,verbose_name='Çağ')
    vote=models.IntegerField(verbose_name='Oy')
    approved=models.BooleanField(default="False",verbose_name='Onay')
    build_list=models.CharField(max_length=1000,verbose_name='Liste şeklinde',default="")  
    def __str__(self):
        return self.headline
class voters(models.Model):
    user1= models.CharField(max_length=100)
    voted=models.IntegerField()
class comments(models.Model):
    pub_date=models.DateTimeField(auto_now=True,verbose_name='Yayınlanma Tarihi')
    comid= models.ForeignKey(Buildorders ,on_delete=models.CASCADE,verbose_name="Build Order'ın No")
    comtext=models.TextField(verbose_name='Yorum')
    comuser=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete= models.CASCADE,verbose_name='Yorumu Yapan Kullanıcı')
    approved=models.BooleanField(default="False",verbose_name="Onay")

    def __str__(self):
        return self.comid.headline