from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('signout/', views.signout, name='signouthome'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signin/signout', views.signout, name='signout'),
    path('signup/home', views.returnhome, name='returnhome'),
    path('signin/signup', views.signupredirect, name='signupredirect'),
    path('signup/signin', views.signin, name='signup-signin'),
    path('signup/signup', views.signup),
    path('signup/signout', views.signout)
]