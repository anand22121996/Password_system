from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)

class Login(models.Model):
	profile = models.CharField(max_length=100)
	username = models.CharField(max_length=255)
	password = models.CharField(max_length=255)
	authorized_user = models.ManyToManyField(User)

	def __str__(self):
		return self.profile