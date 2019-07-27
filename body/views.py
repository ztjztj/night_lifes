from django.shortcuts import render
from django.http import JsonResponse
from .models import BodyNoval
from django.views.decorators.csrf import csrf_exempt

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
#排行榜
def ranking_list(request):
    #获取所有书的信息
    noval = BodyNoval.objects.all()
    #玄幻
    xuanhuan = noval.filter(book_category='玄幻小说').order_by('-book_xiao')
    zong=xuanhuan[:10]
    zhou = xuanhuan[2:12]
    yue =xuanhuan[5:15]
    ri = xuanhuan[:10]

    #修真
    xiuzhen = noval.filter(book_category='修真小说').order_by('-book_xiao')
    zong1=xiuzhen[:10]
    zhou1 = xiuzhen[2:12]
    yue1 = xiuzhen[5:15]
    ri1 = xiuzhen[:10]

    #都市
    dushi = noval.filter(book_category='修真小说').order_by('-book_xiao')
    zong2=dushi[:10]
    zhou2 = dushi[2:12]
    yue2 = dushi[5:15]
    ri2 = dushi[:10]

    #穿越
    chuanyue = noval.filter(book_category='穿越小说').order_by('-book_xiao')
    zong3=chuanyue[:10]
    zhou3 = chuanyue[2:12]
    yue3 = chuanyue[5:15]
    ri3 = chuanyue[:10]

    #网游竞技
    wangyou = noval.filter(book_category='网游小说').order_by('-book_xiao')
    zong4=wangyou[:10]
    zhou4 =wangyou[2:12]
    yue4 = wangyou[5:15]
    ri4 = wangyou[:10]

    #科幻灵异
    kehuan = noval.filter(book_category='科幻小说').order_by('-book_xiao')
    zong5=kehuan[:10]
    zhou5 = kehuan[2:12]
    yue5 = kehuan[5:15]
    ri5 = kehuan[:10]

    #完本小说
    wanben = noval.filter(book_state='完本').order_by('-book_xiao')
    zong6 = wanben[:10]
    zhou6 = wanben[2:12]
    yue6 = wanben[5:15]
    ri6 = wanben[:10]

    #全部小说
    quan = noval.order_by('-book_xiao')
    zong7=quan[:10]
    zhou7 = quan[2:12]
    yue7 = quan[5:15]
    ri7 = quan[:10]

    dict= {
        'zong':zong,'zhou':zhou,'yue':yue,'ri':ri,
        'zong1': zong1, 'zhou1': zhou1, 'yue1': yue1, 'ri1': ri1,
        'zong2': zong2, 'zhou2': zhou2, 'yue2': yue2, 'ri2': ri2,
        'zong3': zong3, 'zhou3': zhou3, 'yue3': yue3, 'ri3': ri3,
        'zong4': zong4, 'zhou4': zhou4, 'yue4': yue4, 'ri4': ri4,
        'zong5': zong5, 'zhou5': zhou5, 'yue5': yue5, 'ri5': ri5,
        'zong6': zong6, 'zhou6': zhou6, 'yue6': yue6, 'ri6': ri6,
        'zong7': zong7, 'zhou7': zhou7, 'yue7': yue7, 'ri7': ri7,
           }


    return render(request, 'ranking_list.html',dict)


def classify(request):

    return render(request, 'classify.html')

def all_book(request):

    return render(request, 'all_book.html')

def retrieve_password(request):

    return render(request, 'retrieve_password.html')