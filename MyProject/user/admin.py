from django.contrib import admin
from .models import *

# Register your models here.
class contactusAdmin(admin.ModelAdmin):
    list_display = ("Name","Email","Mobile","Message")

admin.site.register(contactus,contactusAdmin)
######################################################

class igalleryAdmin(admin.ModelAdmin):
    list_display = ('id','gname','gpic')

admin.site.register(igallery,igalleryAdmin)
#################################################################

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','shead','ssubject','sdes','spic')

admin.site.register(slider,sliderAdmin)
#################################################################
class myblogAdmin(admin.ModelAdmin):
    list_display = ('id','bname','bdes','bpicture','bdate')
admin.site.register(myblog,myblogAdmin)
#################################################################
class ncategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category','cpic','cdate')
admin.site.register(ncategory,ncategoryAdmin)
################################################################
class cityAdmin(admin.ModelAdmin):
    list_display = ('id','ncity','cpic','cdate')
admin.site.register(city,cityAdmin)
###############################################################
class mynewsAdmin(admin.ModelAdmin):
    list_display = ('id','ntitle','nhead','ndes','npic','ncity','category','ndate')
admin.site.register(mynews,mynewsAdmin)

class videonewsAdmin(admin.ModelAdmin):
    list_display = ('id','vlink','vhead','vcategory','vcity','vdate','vdes')
admin.site.register(videonews,videonewsAdmin)


