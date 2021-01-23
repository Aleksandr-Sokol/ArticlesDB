from django.contrib import admin
from .models import Journal, Author, Article

@admin.register(Journal)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name')

@admin.register(Author)
class PostAdmin(admin.ModelAdmin):
    list_display = ('family', 'name')

@admin.register(Article)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'year')