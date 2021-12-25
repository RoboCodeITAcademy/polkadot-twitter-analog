from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
    # path("", views.PostListView.as_view(), name="home"),
    path("", views.index , name="home"),
    path("add/", views.AddPostView.as_view(), name="add"),
    path("category/<str:category_slug>/", views.category_list, name="category_list"),
    path("tag/<str:tag_slug>/", views.tag_list, name="tag_list"),

    path("post/<pk>/", views.PostDetailView.as_view(), name='detail'),

    path("like/", views.like, name="like"),
    path("search/", views.inline_search, name="search"),
    path("up/", views.post_up_down, name='updown'),

]
