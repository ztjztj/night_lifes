from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('bookrack/',views.bookrack,name="bookrack"),
    path('chapter/',views.chapter,name="chapter"),
    path('register/',views.register,name="register"),
    path('article/',views.register,name="article"),
    path('ranking_list/',views.ranking_list,name="ranking_list"),
    path('classify/',views.classify,name="classify"),
    path('all_book/',views.all_book,name="all_book"),
]
