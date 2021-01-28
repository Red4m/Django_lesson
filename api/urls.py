from django.urls import path

from django.conf import settings

from api import views

urlpatterns = [
    path('test/', views.test, name="test"),
    path('articles/', views.ArticleListView.as_view(), name="all_articles"),
    path('articles/<pk>/', views.ArticleDetailView.as_view(), name="get_article"),
    path('users/', views.ProfileListView.as_view(), name="all_users"),
    path('users/<username>/', views.ProfileDetailView.as_view(), name="get_user")
]