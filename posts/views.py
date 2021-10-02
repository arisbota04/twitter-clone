import posts
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from .forms import PostForm
from django import forms
from django.forms.fields import ImageField

# Create your views here.
def index(request):
      #If Method is POST 
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        #If the form is valid
        if form.is_valid():
            # If yes, Save
            form.save()
            #Redirect to Home
            return HttpResponseRedirect('/')          
        else:
            #If no, Show Error
            return HttpResponseRedirect(form.erros.as_json)
    # Get all posts, limit = 20
    posts = Post.objects.all().order_by('-created_at')[:20]
    form = PostForm()
    # Show
    return render(request, 'posts.html',
                    {'posts': posts})

def likes(request, id):
    print(id)
    likedtweet = Post.objects.get(id=id)
    likedtweet.like_count +=1
    likedtweet.save()
    return HttpResponseRedirect("/")
    
def delete(request, post_id):
    #Find the post
    post = Post.objects.get(id = post_id)
    post.delete()
    return HttpResponseRedirect('/')

def edit(request, id):
    if request.method == 'GET':
        posts= Post.objects.get(id=id)
        return render(request, "edit.html", {"posts": posts})
    if request.method == 'POST':
        editposts = Post.objects.get(id=id)
        form =PostForm(request.POST,request.FILES, instance=editposts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
        else:
            return HttpResponse("not valid")