from django.shortcuts import render  
from .models import Post #to access all models/tables

def home(request): 
    posts = Post.objects.all() #getting all the objects
    return render(request, 'index.html', {'posts' : posts})

def post(request, pk):
    clicked_posts = Post.objects.get(id=pk) #get id of the clicked post and assign to pk
    return render(request, 'post.html', { 'clicked_posts' : clicked_posts })

# Create your views here.
