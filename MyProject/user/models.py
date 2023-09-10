from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class contactus(models.Model):
    Name=models.CharField(max_length=100)
    Email=models.CharField(max_length=40)
    Mobile=models.CharField(max_length=30)
    Message=models.TextField()
def __str__(self):
    return self.Name

class slider(models.Model):
    shead=models.CharField(max_length=300)
    ssubject=models.CharField(max_length=500)
    sdes=models.TextField()
    spic=models.ImageField(upload_to='static/slider/',default="")
    def __str__(self):
        return self.shead
############################################################
class igallery(models.Model):
    gname=models.CharField(max_length=400)
    gpic=models.ImageField(upload_to='static/gallery/',default="")


############################################################
class myblog(models.Model):
    bname=models.CharField(max_length=40)
    bdes=models.TextField()
    bpicture=models.ImageField(upload_to='static/blogs',null=True)
    bdate=models.DateField()
############################################################
class ncategory(models.Model):
    category=models.CharField(max_length=80)
    cpic=models.ImageField(upload_to='static/category',null=True)
    cdate=models.DateField()
    def __str__(self):
        return  self.category
############################################################
class city(models.Model):
    ncity=models.CharField(max_length=30)
    cpic=models.ImageField(upload_to='static/city/')
    cdate=models.DateField()
    def __str__(self):
        return self.ncity
###########################################################

class mynews(models.Model):
    ntitle=models.CharField(max_length=500)
    nhead=models.CharField(max_length=500)
    ndes=models.TextField()
    npic=models.ImageField(upload_to='static/news/',null=True)
    ncity=models.ForeignKey(city,on_delete=models.CASCADE,null=True)
    category=models.ForeignKey(ncategory,on_delete=models.CASCADE,null=True)
    ndate=models.DateField()

class videonews(models.Model):
    vlink=models.CharField(max_length=200)
    vhead=models.CharField(max_length=500)
    vcategory=models.CharField(max_length=500)
    vcity=models.CharField(max_length=50)
    vdate=models.DateField()
    vdes=HTMLField()













