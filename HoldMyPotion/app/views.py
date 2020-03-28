from django.shortcuts import render
from app.models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


def article_list(request):
    """Returns the list of all the articles"""
    articles = Article.objects.all().order_by('date')
    return render(
        request,
        'articles/article_list.html',
        {'articles': articles}
    )

def article_detail(request, slug):
    """Returns the detail view of article"""
    article = Article.objects.get(slug=slug)
    return render(
        request,
        'articles/article_detail.html',
        {'article': article}
    )

@login_required(login_url='/accounts/login')
def article_create(request):
    """Creates the article"""
    return render(request, 'articles/article_create.html')
