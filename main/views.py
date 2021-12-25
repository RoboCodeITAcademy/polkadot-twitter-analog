from django.shortcuts import render
from django.http import HttpResponseRedirect,JsonResponse
from django.forms.models import model_to_dict
from django.views.generic.edit import CreateView
from django.views.generic import ListView,DetailView
from django.core.paginator import Paginator
from telepot import Bot
from .models import Post ,Category, Tag , Like
bot = Bot("YOUR TOKEN")
grID = "YOUR GROUP ID"

# Create your views here.
# class PostListView(ListView):
#     model = Post
#     template_name = 'app.html'
#     context_object_name = "posts"
#     paginate_by = 1 # contextda page_obj bolib ketadi


def index(request):
    # bot.sendMessage(grID , "Qale")
    posts = Post.objects.all()
    paginator = Paginator(posts, 2)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "app.html",{"page_obj":page_obj})

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

class PostDetailView(DetailView):
    model = Post
    # template_name = 'detail.html'


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
    d = json.loads(request.GET["data"])
    queryset = list(Post.objects.filter(title__icontains=d).values())
    data = {}
    data["object_list"] = queryset

    return JsonResponse(data)

def post_up_down(request):
    d = json.loads(request.GET["data"])
    print(d)
    post = Post.objects.get(id=int(d["post_id"]))
    profile = request.user.profile
    if d["statement"] == "up":
        if post not in profile.likes.all():
            post.up += 1
            profile.likes.add(post)
            post.save()
            profile.save()
            # bot.sendMessage(grID, "Like")
    if d["statement"] == "down":
        if post not in profile.likes.all():
            post.down += 1
            profile.likes.add(post)
            post.save()
            profile.save()
            # bot.sendMessage(grID, "Dislike")
    return JsonResponse({"post_up":post.up, "post_down":post.down})
