from django.urls import path, include

from django.conf import settings
from rest_framework.routers import DefaultRouter


from api import views

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename="articles")
router.register('users', views.UserViewSet, basename="users")
"""
/articles/  GET / LIST
/articles/  POST / CREATE
/articles/<int:pk>/ GET / Read
/articles/<int:pk>/ 
/articles/<int:pk>/
"""
urlpatterns = [
    path('', include(router.urls)),

    # path('test/', views.test, name="test"),
    # path('articles/', views.ArticleListView.as_view(), name="all_articles"),
    # path('articles/<pk>/', views.ArticleDetailView.as_view(), name="get_article"),
    # path('users/', views.ProfileListView.as_view(), name="all_users"),
    # path('users/<username>/', views.ProfileDetailView.as_view(), name="get_user")
]