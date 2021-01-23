from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from home.models import Article


def home(request):
    return HttpResponse("<b>Hello</b> world")


def age(request):
    return HttpResponse("age")


def user(request):
    return HttpResponse(f"igor is user ")


def username(request, username):
    return HttpResponse(f"chvyrov {username}")


def debug(request):
    # import pdb; pdb.set_trace()
    page = request.GET.get('page')
    return HttpResponse(f"debugger page {page}")


@login_required
def all_articles(request):
    print(request.user.username)
    if request.user.is_authenticated:
        articles = Article.objects.all()
        return render(
            request, "article.html", {"articles": articles},
        )
    else:
        return HttpResponse(f"You are not logged in", 404)


def get_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # article = Article.objects.get(pk=pk)
    # return HttpResponse(article)
    return render(
        request, "one_article.html", {"article": article},
    )


def edit_article(request, pk):
    # print(request.POST)
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # article.pk = request.POST.get('pk')
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
    return render(
        request, "edit_article.html", {"article": article},
    )