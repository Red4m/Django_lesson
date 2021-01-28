from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import serializers

from home.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['id', 'title', 'content', 'author', 'link']

    def get_link(self, obj):
        uri = reverse('get_article', kwargs={'pk': obj.pk})
        return self.context['request'].build_absolute_uri(uri)


class ProfileSerializer(serializers.ModelSerializer):
    articles = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id', 'username', 'articles', 'link'
                  ]

    def get_articles(self, obj):
        articles = Article.objects.all().filter(author=obj)
        s = ArticleSerializer(articles, many=True, context=self.context)
        return s.data

    def get_link(self, obj):
        uri = reverse('get_user', kwargs={'username': obj.username})
        return self.context['request'].build_absolute_uri(uri)
        # return f"http://localhost:8000{uri}"
