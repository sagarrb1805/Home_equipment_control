from django.urls import path
from . import views

urlpatterns = [
    path('api/<str:user>/get', views.getData),
    path('api/<str:user>/put', views.putData),

]