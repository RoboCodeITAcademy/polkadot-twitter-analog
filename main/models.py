from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
	title = models.CharField('Category name *',max_length=50)
	slug = models.SlugField('*',max_length=25, unique=True)

	class Meta:
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'

	def __str__(self):
		return "{}".format(self.title)

class Tag(models.Model):
	title = models.CharField('Tag name *',max_length=50)
	slug = models.SlugField('*',max_length=25, unique=True)

	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tags'

	def __str__(self):
		return "{}".format(self.title)


class Post(models.Model):
    body = RichTextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    up = models.PositiveIntegerField(default=0)
    down = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, related_name='categories')
    tag = models.ManyToManyField(Tag, related_name='tags')
    published = models.DateTimeField(auto_now_add=True)