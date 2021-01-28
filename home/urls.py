from django.contrib import admin
from django.urls import path

from django.conf import settings

from api import urls
from home import views
from home import views

urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name="articles"),

    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name="get_article"),
    path('articles/<int:pk>/edit/', views.ArticleUpdateView.as_view(), name="edit_article")
]


