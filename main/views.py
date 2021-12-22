from django.shortcuts import render
from django.views.generic.edit import CreateView

from .models import Post
# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, "app.html",{"posts":posts})

class AddPostView(CreateView):
    model = Post
    fields = ('category', 'tag','body')
    template_name = "polkadots/add.html"
    success_url = "/"