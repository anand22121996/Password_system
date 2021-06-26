from django.urls import path
from app import views
from django.contrib.auth import views as auth_views

urlpatterns = [
		path('',views.home,name='home'),
		path('form/',views.form,name='form'),
		path('detail/<int:id>/',views.decryptpass,name='detail'),
		path('signup/',views.signup,name='signup'),
		path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='signin'),
		path('sharepass/<int:id>/',views.sharepass,name='sharepass'),
		path('share/<int:id>/<int:lid>/',views.share,name='share'),
		path('logout/',views.logoutview,name='logout'),
		path('remove/<int:id>/<int:lid>/',views.remove,name='remove'),
		path('delete/<int:id>./',views.delete_profile,name='delete'),
		path('loginprofile/<int:id>/',views.loginbutton,name='login'),

]
