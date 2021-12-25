from django.db import models
from django.conf import settings
from main.models import Post
# from main.models import Post
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=None, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    follower = models.PositiveIntegerField(default=0)
    post = models.PositiveIntegerField(default=0)
    rank = models.CharField(max_length=200, blank=True)
    short_info = models.CharField(max_length=200, blank=True)
    likes = models.ManyToManyField(Post, related_name='post_likes')
    user_icon = models.CharField("Fontawesome User icon name", max_length=50, blank=True)
    # liked_post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name = "liked_posts")

    def image_url(self):
        if self.photo:
            return getattr(self.photo, 'url', "/static/img/nouser.png")
        return None


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)
