from django.contrib import admin
from django.urls import path

from django.conf import settings

from home import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', views.home, name='home'),
    # path('name/', views.user, name='name'),
    #
    # path('age/', views.age, name='age'),
    # path('debug/', views.debug, name="debug"),
    #
    #
    # path('gena/', views.user, name="petr"),

    path('articles/', views.ArticleListView.as_view(), name="articles"),

    path('articles/<int:pk>/', views.ArticleDetailView.as_view(), name="get_article"),
    path('articles/<int:pk>/edit/', views.edit_article, name="edit_article")


    # path('<username>/', views.username, name='username'),

]

