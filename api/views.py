from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render

from api.serializers import ArticleSerializer, ProfileSerializer
from home.models import Article
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView


def test(request):
    return JsonResponse(
        {
            'date': '2020-12-21',
            'group': 'igor',
        }
    )


class ArticleListView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ProfileListView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer


class ProfileDetailView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    lookup_field ="username"
    serializer_class = ProfileSerializer


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
