from django.shortcuts import render

def index(request):
    return render(request, 'index.html')
# Create your views here.

def bookrack(request):
    return render(request, 'bookrack.html')

def chapter(request):
    return render(request, 'chapter.html')

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