from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.forms.models import model_to_dict
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from .models import Post ,Category, Tag , Like


# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "app.html",{"posts":posts})

class AddPostView(CreateView):
    model = Post
    fields = ('category', 'tag','body')
    template_name = "main/add.html"
    success_url = "/"
    
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author= self.request.user
        obj.save()        
        return HttpResponseRedirect(self.success_url)
    
def category_list(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    object_list = Post.objects.filter(category=category)
    
    context = {
        "object_list":object_list
    }
    return render(request, "main/list.html",context)

def tag_list(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    object_list = Post.objects.filter(tag=tag)
    
    context = {
        "object_list":object_list
    }
    return render(request, "main/list.html",context)

import json
from datetime import datetime
def like(request):
    data = json.loads(request.GET["data"])
    postId = data["post_id"]
    post = Post.objects.get(id=postId)
    user = request.user
    
    # if Like.objects.filter(user=user, post=post).exists():
    #     Like.alreadyLiked = True
    #     return JsonResponse({"status":404})
    
    like = Like.objects.create(user=user,post=post)
    like.alreadyLiked = True
    post.up += 1
    post.save()
    like.save()
    return JsonResponse({"status":200})

def inline_search(request):
    data = json.loads(request.GET["data"])
    posts = Post.objects.filter(body__icontains=data).values()
    # d  = json.dumps({"data":posts})
    
    
    return JsonResponse({"data":d})
    