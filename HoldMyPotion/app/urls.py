from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    # path('about/', views.about_page, name='about_page'),
]
