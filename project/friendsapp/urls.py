from django.urls import path
from friendsapp import views


urlpatterns = [
    path('',views.home,name='home'),
]
