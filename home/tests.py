from django.test import TestCase

from home.models import Article


class ArticleTestCase(TestCase):

    def test_create_article(self):
        Article.objects.create(
            title="Test title",
            content="test content",
        )
        self.assertEqual(Article.objects.count(), 1)

    def test_api_get_article(self):
        pass