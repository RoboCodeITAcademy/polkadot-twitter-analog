from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug']
	prepopulated_fields = {'slug':('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ['category','author','up', 'down', 'active']
	list_filter = ['up', 'author',"published"]
 
admin.site.register(Like)