from django.contrib import admin
from home.models import Article

# Register your models here.
# admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author')
    search_fields = ('title',)

