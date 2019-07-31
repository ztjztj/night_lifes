from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('exit/',views.exit,name='exit'),   #注销账号
    path('bookrack/',views.bookrack,name="bookrack"), #书架
    path('chapter/',views.chapter,name="chapter"),
    path('chapter_ajax',views.chapter_ajax,name = "chapter_ajax"),
    path('register/',views.register,name="register"),  #注册
    path('article/',views.article,name="article"),
    path('ranking_list/',views.ranking_list,name="ranking_list"),
    path('classify/<str:classify>/',views.classify,name="classify"),
    path('all_book/',views.all_book,name="all_book"),
    path('retrieve_password/',views.retrieve_password,name="retrieve_password"),
    path('article_ajax/',views.article_ajax,name="article_ajax"),
    path('verify/',views.verify,name='verify'),    #验证
    path('add_bookrack_ajax/',views.add_bookrack_ajax,name='add_bookrack_ajax'), #添加书架ajax


]
