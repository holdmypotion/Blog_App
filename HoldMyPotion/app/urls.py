from django.urls import path

from app import views

app_name = 'app'

urlpatterns = [
    path('', views.article_list, name='list'),
    path('<str:slug>/', views.article_detail, name='article_detail'),
]
