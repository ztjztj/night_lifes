from django.shortcuts import render
from body import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
def index(request):
    return render(request, 'index.html')
# Create your views here.

def bookrack(request):
    return render(request, 'bookrack.html')


def chapter(request):

    all = models.Noval_room.objects.filter(book_foreign="http://www.xbiquge.la/14/14963/").order_by("book_chapter_id")
    return render(request, 'chapter.html',{"all":all})



def register(request):
    return render(request, 'register.html')

def article(request):
    book = "http://www.xbiquge.la/14/14963/"
    chapter = '0'
    info = models.Noval_room.objects.filter(book_foreign=book,book_chapter_id=chapter).values()
    info = list(info)[0]
    info['book_content'] = str(info['book_content']).replace('\r','')
    return render(request, 'article.html', {"info": info})

@csrf_exempt
def article_ajax(request):
    paramter = request.POST
    book = paramter.get('book')
    chapter = paramter.get('chapter')
    info = models.Noval_room.objects.filter(book_foreign=book,book_chapter_id=chapter).values()
    info = list(info)[0]
    info['book_content'] = str(info['book_content']).replace('\r','')
    return JsonResponse(info)

def ranking_list(request):

    return render(request, 'ranking_list.html')
def classify(request):

    return render(request, 'classify.html')

def all_book(request):

    return render(request, 'all_book.html')

def retrieve_password(request):

    return render(request, 'retrieve_password.html')