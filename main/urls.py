from django.urls import path
from .import views

app_name = "main"

urlpatterns = [
    path("", views.index, name="home"),
    path("add/", views.AddPostView.as_view(), name="add"),

]