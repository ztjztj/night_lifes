from django.shortcuts import render,HttpResponse
from .models import *
from .import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def exit(request):
    request.session.flush()
    return redirect(index)



@csrf_exempt     #ajax的csrf验证
def index(request):
    if request.method =='GET':
        if request.session.has_key('userNumber'):
            user_name =request.session['user_name']
            return render(request,'index.html',{'user_name':user_name})
        else:
            return render(request,'index.html')

    else:
        userNumber = request.POST.get('userNumber')
        password = request.POST.get('password')
        print(userNumber,password)
        # user = models.BodyUser.objects.get(userNumber=userNumber,password=password)

        try:
            user = models.BodyUser.objects.get(userNumber=userNumber,password=password)
        except  models.BodyUser.DoesNotExist:
            user=None

        print('user='+str(user))
        if user != None:
            request.session['userNumber'] = userNumber
            request.session['passwprd'] = password
            request.session['user_name'] = user.user_name
            user_name = request.session['user_name']
            print('user_name=',user_name)
            return render(request, 'index.html', {'user_name': user_name})
            # return JsonResponse({'user_name':user_name})
        else:
            return render(request, 'index.html')
            # return JsonResponse({'user_name':'用户名或者密码错误'})




def register(request):        #注册
    if request.method=='GET':
        return render(request,'register.html')
    else:
        userNumber = request.POST.get('userNumber')
        password =request.POST.get('password')
        password2 =request.POST.get('password')
        user_name =request.POST.get('user_name')
        email =request.POST.get('email')
        sex =request.POST.get('sex')
        qq =request.POST.get('qq')

        print(userNumber,password,password2,email,sex,qq)

        bodyuser =models.BodyUser()
        bodyuser.userNumber=userNumber
        bodyuser.password =password
        bodyuser.user_name=user_name
        bodyuser.email=email
        bodyuser.sex=sex
        bodyuser.qq =qq

        bodyuser.save()
        return render(request, 'index.html')


def verify(request):
    type = request.POST.get('type')
    data=request.POST.get('data')
    error_type = request.POST.get('error_type')
    print(type,data)
    if type =='账号':
        if data =='':
            return JsonResponse({'verify':'账号不能为空','error_types':error_type})
        else:
            try:
                user = models.BodyUser.objects.get(userNumber=data)
            except models.BodyUser.DoesNotExist:
                user =None
            if user ==None:
                return JsonResponse({'verify':'账号暂未注册，可以使用','error_types':error_type})
            else:
                return JsonResponse({'verify':'账号已被注册，请您更换账号','error_types':error_type})
    elif type =='密码':

        if data == '':
            return JsonResponse({'verify': '密码不能为空','error_types':error_type})
        else:
            return JsonResponse({'verify': '请记住您输入的密码','error_types':error_type})

    elif type =='用户名':
        if data == '':
            return JsonResponse({'verify': '用户名不能为空','error_types':error_type})
        else:
            try:
                user =models.BodyUser.objects.get(user_name=data)
            except models.BodyUser.DoesNotExist:
                user =None
            if user==None:
                return JsonResponse({'verify':'该用户名可以使用','error_types':error_type})
            else:
                return JsonResponse({'verify':'该用户名已被使用','error_types':error_type})

    elif type =='邮箱':
        if data == '':
            return JsonResponse({'verify': '邮箱不能为空','error_types':error_type})
        else:
            try:
                user =models.BodyUser.objects.get(email=data)
            except models.BodyUser.DoesNotExist:
                user =None
            if user==None:
                return JsonResponse({'verify':'该邮箱可以使用','error_types':error_type})
            else:
                return JsonResponse({'verify':'该邮箱已被使用','error_types':error_type})
    else:
        return JsonResponse({'verify':'请输入正确内容','error_types':error_type})


def bookrack(request):   #书架

    if request.session.has_key('userNumber'):
        user_name =request.session['user_name']
        return render(request,'bookrack.html',{'user_name':user_name})
    else:
        return render(request,'bookrack.html')


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

    if request.session.has_key('userNumber'):
        user_name =request.session['user_name']
        return render(request, 'chapter.html', {'chapter_info': chapter_info, 'chapter_list': chapter_list,'page':1,'book_id':book_id,'user_name':user_name})
    else:
        return render(request, 'chapter.html',
                      {'chapter_info': chapter_info, 'chapter_list': chapter_list, 'page': 1, 'book_id': book_id})


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

    chapter_info = models.BodyNoval.objects.filter(id =book_id)[0]
    chapter_list = models.ChapterUrls.objects.filter(book_url=chapter_info.book_url).order_by('chapter_id').values()
    chapter_list = chapter_list[(int(page)-1)*102:int(page)*102].values()
    chapter_list = list(chapter_list)
    info = {'chapter_list':chapter_list,'page':int(page),'book_id':int(book_id)}

    return JsonResponse(info)


def article(request):   #文章内容
    book_id = request.GET.get('id')
    chapter = request.GET.get('chapter')
    book = models.BodyNoval.objects.get(id=book_id)
    book_category =request.GET.get('book_category')
    book_name=request.GET.get('book_name')
    info = models.Noval_room.objects.filter(book_foreign=book.book_url,book_chapter_id=chapter).values()
    try:
        info = list(info)[0]
        info['book_content'] = str(info['book_content']).replace('\r', '')
    except IndexError:
        info = {'book_section':'暂无此章内容'}
    if request.session.has_key('userNumber'):
        user_name =request.session['user_name']
        return render(request, 'article.html', {"info": info,'book_id':book_id,'book_category':book_category,'book_name':book_name,'user_name':user_name})
    else:
        return render(request, 'article.html', {"info": info,'book_category':book_category,'book_name':book_name,'book_id': book_id})

@csrf_exempt
def article_ajax(request):     #文章内容ajax
    paramter = request.POST
    book = paramter.get('book')
    chapter = paramter.get('chapter')
    info = models.Noval_room.objects.filter(book_foreign=book,book_chapter_id=chapter).values()
    info = list(info)[0]
    info['book_content'] = str(info['book_content']).replace('\r','')
    return JsonResponse(info)

def ranking_list(request):    #排行榜

    # 获取所有书的信息
    noval = BodyNoval.objects.all()

    # 玄幻
    xuanhuan = noval.filter(book_category='玄幻小说').order_by('-book_xiao')
    zong = xuanhuan[:10]
    zhou = xuanhuan[2:12]
    yue = xuanhuan[5:15]
    ri = xuanhuan[11:21]

    # 修真
    xiuzhen = noval.filter(book_category='修真小说').order_by('-book_xiao')
    zong1 = xiuzhen[:10]
    zhou1 = xiuzhen[2:12]
    yue1 = xiuzhen[5:15]
    ri1 = xiuzhen[11:21]

    # 都市
    dushi = noval.filter(book_category='修真小说').order_by('-book_xiao')
    zong2 = dushi[:10]
    zhou2 = dushi[2:12]
    yue2 = dushi[5:15]
    ri2 = dushi[11:21]

    # 穿越
    chuanyue = noval.filter(book_category='穿越小说').order_by('-book_xiao')
    zong3 = chuanyue[:10]
    zhou3 = chuanyue[2:12]
    yue3 = chuanyue[5:15]
    ri3 = chuanyue[11:21]

    # 网游竞技
    wangyou = noval.filter(book_category='网游小说').order_by('-book_xiao')
    zong4 = wangyou[:10]
    zhou4 = wangyou[2:12]
    yue4 = wangyou[5:15]
    ri4 = wangyou[11:21]

    # 科幻灵异
    kehuan = noval.filter(book_category='科幻小说').order_by('-book_xiao')
    zong5 = kehuan[:10]
    zhou5 = kehuan[2:12]
    yue5 = kehuan[5:15]
    ri5 = kehuan[11:21]

    # 完本小说
    wanben = noval.filter(book_state='完本').order_by('-book_xiao')
    zong6 = wanben[:10]
    zhou6 = wanben[2:12]
    yue6 = wanben[5:15]
    ri6 = wanben[11:21]

    # 全部小说
    quan = noval.order_by('-book_xiao')
    zong7 = quan[:10]
    zhou7 = quan[2:12]
    yue7 = quan[5:15]
    ri7 = quan[11:21]

    dict1 = {
        'zong': zong, 'zhou': zhou, 'yue': yue, 'ri': ri,
        'zong1': zong1, 'zhou1': zhou1, 'yue1': yue1, 'ri1': ri1,
        'zong2': zong2, 'zhou2': zhou2, 'yue2': yue2, 'ri2': ri2,
        'zong3': zong3, 'zhou3': zhou3, 'yue3': yue3, 'ri3': ri3,
        'zong4': zong4, 'zhou4': zhou4, 'yue4': yue4, 'ri4': ri4,
        'zong5': zong5, 'zhou5': zhou5, 'yue5': yue5, 'ri5': ri5,
        'zong6': zong6, 'zhou6': zhou6, 'yue6': yue6, 'ri6': ri6,
        'zong7': zong7, 'zhou7': zhou7, 'yue7': yue7, 'ri7': ri7,
    }
    if request.session.has_key('userNumber'):   #判断当前是否有账号信息
        user_name = request.session['user_name']
        dict2 = {
            'user_name':user_name,
            'zong': zong, 'zhou': zhou, 'yue': yue, 'ri': ri,
            'zong1': zong1, 'zhou1': zhou1, 'yue1': yue1, 'ri1': ri1,
            'zong2': zong2, 'zhou2': zhou2, 'yue2': yue2, 'ri2': ri2,
            'zong3': zong3, 'zhou3': zhou3, 'yue3': yue3, 'ri3': ri3,
            'zong4': zong4, 'zhou4': zhou4, 'yue4': yue4, 'ri4': ri4,
            'zong5': zong5, 'zhou5': zhou5, 'yue5': yue5, 'ri5': ri5,
            'zong6': zong6, 'zhou6': zhou6, 'yue6': yue6, 'ri6': ri6,
            'zong7': zong7, 'zhou7': zhou7, 'yue7': yue7, 'ri7': ri7,
        }
        return render(request, 'ranking_list.html',dict2)
    else:
        return render(request, 'ranking_list.html', dict1)

def classify(request):
    return render(request, 'ranking_list.html',dict)

#分类页面
def classify(request,classify):
    # print(classify)
    #查找所有类别的小说
    noval = BodyNoval.objects.filter(book_category=classify)
    # 展示图片的6个小说
    zhans = noval[:6]
    # 展示最近更新的小说
    updata = noval.order_by('book_update')[0:30]
    # 好看的玄幻小说
    hao = noval.order_by('-id')[0:30]
    return render(request,'classify.html',{'classify':classify,'zhans':zhans,'updata':updata,'hao':hao})


def all_book(request):

    return render(request, 'all_book.html')

def retrieve_password(request):

    return render(request, 'retrieve_password.html')