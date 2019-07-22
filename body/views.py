from django.shortcuts import render

def index(request):
    return render(request,'笔趣阁首页.html')
# Create your views here.

def bookrack(request):
    return render(request,'笔趣阁书架.html')

def chapter(request):
    return render(request,'章节信息页面.html')

def register(request):
    return render(request,'注册页面.html')

def article(request):

    return render(request, '文章页面信息.html')

def ranking_list(request):

    return render(request, '排行榜单.html')
def classify(request):

    return render(request, '分类页面展示.html')

def all_book(request):

    return render(request, '全部小说.html')