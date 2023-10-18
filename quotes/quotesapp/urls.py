from django.urls import path
from . import views

app_name = 'quotesapp'

urlpatterns = [
    path('', views.main, name='main'),
    path('tag/', views.tag, name='tag'),
    path('quote/', views.quote, name='quote'),
    path('author/', views.author, name='author'),
    path('detail/<int:quote_id>', views.detail, name='detail'),
    path('about_author/<int:author_id>',
         views.about_author, name='about_author'),
]
