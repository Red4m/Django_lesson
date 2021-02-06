from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from api.pagination import CustomPageNumberPagination
from api.permissions import IsAuthorOrReadOnly,IsUserOrReadOnly
from api.serializers import ArticleSerializer, ProfileSerializer, \
    UserSerializer
from home.models import Article
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

def test(request):
    return JsonResponse(
        {
            'date': '2020-12-21',
            'group': 'igor',
        }
    )

#### new way #####


class ArticleViewSet(ModelViewSet):
    # permission_classes = (IsAuthenticated, IsAuthorOrReadOnly, )
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (SearchFilter, )
    search_fields = ('title', 'content')


#### new way #####


class UserViewSet(ModelViewSet):
    permission_classes = (IsAdminUser, IsUserOrReadOnly, )
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "username"
    pagination_class = LimitOffsetPagination

###### old way ######


# class ArticleListView(ListCreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#
# class ArticleDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer



###### old way ######


# class ProfileListView(ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = ProfileSerializer
#
#
# class ProfileDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     lookup_field ="username"
#     serializer_class = ProfileSerializer
#

#
# def all_articles(request):
#     articles = Article.objects.all()
#     s = ArticleSerializer(articles, many=True)
#     return JsonResponse(s.data, safe=False)
#
#
# def get_article(request, pk):
#     article = Article.objects.filter(pk=pk)
#     s = ArticleSerializer(article, many=True)
#     return JsonResponse(s.data, safe=False)
