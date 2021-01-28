from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, UpdateView

from home.models import Article


# def home(request):
#     return HttpResponse("<b>Hello</b> world")
#
#
# def age(request):
#     return HttpResponse("age")
#
#
# def user(request):
#     return HttpResponse(f"igor is user ")
#
#
# def username(request, username):
#     return HttpResponse(f"chvyrov {username}")
#
#
# def debug(request):
#     # import pdb; pdb.set_trace()
#     page = request.GET.get('page')
#     return HttpResponse(f"debugger page {page}")


# @login_required
# def all_articles(request):
#     print(request.user.username)
#     if request.user.is_authenticated:
#         articles = Article.objects.all()
#         return render(
#             request, "article.html", {"articles": articles},
#         )
#     else:
#         return HttpResponse(f"You are not logged in", 404)


# def get_article(request, pk):
#     article = get_object_or_404(Article, pk=pk)
#     # article = Article.objects.get(pk=pk)
#     # return HttpResponse(article)
#     return render(
#         request, "one_article.html", {"article": article},
#     )
class ArticleListView(ListView):
    model = Article
    template_name = "article.html"
    ordering = "title"
    context_object_name = "articles"


class ArticleDetailView(DetailView):
    model = Article
    template_name = "one_article.html"
    pk_url_kwarg = "pk"
    context_object_name = "article"

# class GetArticleView(TemplateView):
#     template_name = "one_article.html"
#
#     def get_context_data(self, pk, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['article'] = get_object_or_404(Article, pk=pk)
#         return context


# def edit_article(request, pk):
#     # print(request.POST)
#     article = get_object_or_404(Article, pk=pk)
#     if request.method == 'POST':
#         # article.pk = request.POST.get('pk')
#         article.title = request.POST.get('title')
#         article.content = request.POST.get('content')
#         article.save()
#     return render(
#         request, "edit_article.html", {"article": article},
#     )


class ArticleUpdateView(UpdateView):
    model = Article
    slug_field = "title"
    slug_url_kwarg = "title"
    template_name = "edit_article.html"
    success_url = "/articles/"
    context_object_name = "article"
    fields = ['title', 'content', 'author']


