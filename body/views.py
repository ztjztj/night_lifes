from django.shortcuts import render,HttpResponse
from .models import *
from .import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'index.html')


def bookrack(request):
    return render(request, 'bookrack.html')


# 章节信息
def chapter(request):
    """

    :param request:
    :return:
    """

    request_list = request.GET
    book_id = request_list.get('id')


    chapter_info = models.BodyNoval.objects.filter(id=int(book_id))[0]
    chapter_list = models.ChapterUrls.objects.filter(book_url=chapter_info.book_url).order_by('chapter_id')
    chapter_list = chapter_list[0:102]

    return render(request, 'chapter.html', {'chapter_info': chapter_info, 'chapter_list': chapter_list,'page':1,'book_id':book_id})



# 使用ajax跳转章节分页
@csrf_exempt
def chapter_ajax(request):
    """
    #
    # print(a)
    # book_id = 250
    # page = 3
    开始页面  102*（页数-1）
    结束页面  102*（页数）
    :param request:
    :return:
    """
    request_list = request.POST
    book_id = request_list.get('id')
    page = request_list.get('page')

    chapter_info = models.BodyNoval.objects.filter(id = book_id)[0]
    chapter_list = models.ChapterUrls.objects.filter(book_url=chapter_info.book_url).order_by('chapter_id').values()
    chapter_list = chapter_list[(int(page)-1)*102:int(page)*102].values()
    chapter_list = list(chapter_list)
    info = {'chapter_list':chapter_list,'page':int(page),'book_id':int(book_id)}

    return JsonResponse(info)





def register(request):
    return render(request, 'register.html')

def article(request):

    return render(request, 'article.html')

def ranking_list(request):

    return render(request, 'ranking_list.html')
def classify(request):

    return render(request, 'classify.html')

def all_book(request):

    return render(request, 'all_book.html')

def retrieve_password(request):

    return render(request, 'retrieve_password.html')