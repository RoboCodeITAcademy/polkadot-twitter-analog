from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
    follower = models.PositiveIntegerField(default=0)
    post = models.PositiveIntegerField(default=0)
    rank = models.CharField(max_length=200, blank=True)
    short_info = models.CharField(max_length=200, blank=True)
    likes = models.PositiveIntegerField("Polkadots count", default=0)
    user_icon = models.CharField("Fontawesome User icon name", max_length=50, blank=True)


    def __str__(self):
        return 'Profile for user {}'.format(self.user.username)