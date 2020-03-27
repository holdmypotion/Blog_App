from django.shortcuts import render
from app.models import Article


def article_list(request):
    """Returns the list of all the articles"""
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})
