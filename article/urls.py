from django.urls import path
from article.views import *

app_name = 'article'

urlpatterns=[
    path('',article, name='article'),
    path('json/comments',get_comments_json,name='get_comments_json'),
    path('json/article',get_article_json,name='get_article_json'),
    path('add_article/',add_article,name='add_article'),
    path('<slug:slug>/',detail, name='detail'),
    path('add_comment/',add_comment, name='add_comment'),

    
]