from django.contrib import admin
from . models import Login

# Register your models here.
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
# 	model = Profile
# 	list_display = ['id','user']


@admin.register(Login)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ['id','profile','username','password']
	list_display_links = ('profile',)



