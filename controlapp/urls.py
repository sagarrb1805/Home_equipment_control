from unicodedata import name
from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signin/signout', views.signout, name='signout'),
    path('signup/home', views.returnhome, name='returnhome')
]