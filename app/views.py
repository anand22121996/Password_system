from django.contrib.messages.api import success
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Login
from cryptography.fernet import Fernet
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import logout
from .forms import UserRegisterForm
from selenium import webdriver
from getpass import getpass
import time

#load secret Key function
def load_key():
    return open('secret.key','rb').read()

#encrypt message function
def encrypt_message(message):
    key = load_key()
    encoded_msg = message.encode()
    f = Fernet(key)
    encoded_msg = f.encrypt(encoded_msg)
    # print(encoded_msg)
    return encoded_msg

#decrypt message function
def decrypt_message(enc_msg):
    key = load_key()
    f = Fernet(key)
    dec_msg = f.decrypt(enc_msg)
    return dec_msg.decode()





# home function
@login_required(login_url='signin')
def home(request):
	login = Login.objects.all()
	assigned_pass = Login.objects.filter(authorized_user=request.user)
	context = {'login':login,'assigned_pass':assigned_pass}

	return render(request,'app/home.html',context=context)

#Profile form function
@login_required(login_url='signin')
def form(request):
	if request.user.is_superuser:
		if request.method == 'POST':
			form = LoginForm(request.POST)
			if form.is_valid():
				profile = form.cleaned_data['profile']
				username = form.cleaned_data['username']
				a = encrypt_message(form.cleaned_data['password'])
				password = a.decode('utf-8')
				# print(password)
				password1 = form.cleaned_data['password']
				print(password1)

				obj = Login(profile=profile,username=username,password=password)
				obj.save()
				messages.success(request, f'{profile} -  Profile has been saved')
				return redirect('/')

		form = LoginForm()
		context = {'form':form}
		return render(request,'app/form.html',context=context)
	else:
		return redirect('userpass')

#decrypt request function
def decryptpass(request,id):
	login = Login.objects.get(id=id)
	a = login.password
	# print(a)
	password = decrypt_message(a.encode())

	context = {'login':login,'password':password}	

	return render(request,'app/detail.html',context=context)	

#signup function
def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('signin')
    else:
        form = UserRegisterForm()
    return render(request, 'app/register.html', {'form': form})


#sharepassword function
@login_required(login_url='signin')
def sharepass(request,id):
	users = User.objects.all()
	obj = Login.objects.get(id=id)
	assigned = obj.authorized_user.all()
	context = {'users':users,'obj':obj,'assigned':assigned}
	return render(request,'app/sharepass.html',context=context)

#Password Share function
@login_required(login_url='signin')
def share(request,id,lid):
	user = User.objects.get(id=id)
	login = Login.objects.get(id=lid)
	login.authorized_user.add(user)	
	messages.success(request, f'Profile has been shared with {user}')
	return redirect('sharepass',id=lid)

#logout view
@login_required(login_url='signin')
def logoutview(request):
	logout(request)
	return redirect('/')

#remove user function
@login_required(login_url='signin')
def remove(request,id,lid):
	user = User.objects.get(id=id)
	login = Login.objects.get(id=lid)
	login.authorized_user.remove(user)
	messages.success(request, f'{login} \tProfile has been removed from {user}')
	return redirect('sharepass',id=lid)


#delete profile function
@login_required(login_url='signin')
def delete_profile(request,id):
	login = Login.objects.get(id=id)
	login.delete()
	messages.success(request, f'{login}-Profile has been deleted')
	return redirect('/')

def loginbutton(request,id):
	login = Login.objects.get(id=id)
	profile = login.profile
	username = login.username
	passw = login.password
	

	driver = webdriver.Chrome("C:/chromedriver.exe")
	driver.get('https://www.facebook.com/')

	username = username
	password = decrypt_message(passw.encode())

	usernamebox = driver.find_element_by_id('email')
	usernamebox.send_keys(username)

	password1 = driver.find_element_by_id('pass')
	password1.send_keys(password)

	login = driver.find_element_by_name("login")
	login.click()

	time.sleep(25)

	driver.close()

	return redirect('/')
