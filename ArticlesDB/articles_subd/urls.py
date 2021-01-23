from django.urls import path

from . import views

app_name = 'articles_subd'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/files', views.add_files),
    path('add/journal/', views.JournalCreateView.as_view()),
    path('add/author/', views.AuthorCreateView.as_view()),
    path('add/article/', views.ArticleCreateView.as_view()),
]