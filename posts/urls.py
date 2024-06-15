from django.urls import path
from . import views #import views

urlpatterns = [
    path('', views.home, name='home'), #path:home url, when user comes home is directed to home def in the views.py
    path('post/<str:pk>', views.post, name='post') # dynamic url when user clicks blog to display post/1
] 