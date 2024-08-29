from django.shortcuts import render, HttpResponse, redirect
from app01 import models
from urllib3 import request

from app01.models import UserInfo


# Create your views here.


def index(request):
    return HttpResponse(' 欢迎使用 ')


def user_list(request):
    return render(request, 'user_list.html')


def user_del(request):
    return HttpResponse('这里将实现一个用户注销功能')


def tpl(request):
    name = 'Sunrise'
    roles = ['boss', 'CEO', 'Queen']
    user_info = {'name': "Sunrise", 'salary':500000, 'role':"Queen"}

    data_list = [
        {'name': "Blip", 'salary': 100000, 'role': "normal"},
        {'name': "Zero", 'salary': 200000, 'role': "ALL"},
        {'name': "Ole", 'salary': 300000, 'role': "King"}
    ]

    return render(request,
                  'tpl.html',
                  {'string': name, 'list': roles, 'dictionary': user_info, 'dic_list': data_list}
                  )


def something(request):
    #   request是一个对象，封装了用户发送的所有请求相关数据

    #   1.用request.method获取请求方式
    print(request.method)
    #   2.获取在URL上传递的值 ?n1=999&n2=777
    #   <QueryDict: {'n1': ['999'], 'n2': ['777']}>
    print(request.GET)
    #   3.在请求体中提交数据数据
    print(request.POST)

    #   4.【响应】HttpResponse("返回内容") 将字符串内容返回给用户
    # return HttpResponse("返回内容")

    #   5.【响应】读取html内容 + 渲染（替换）-> 字符串，返回给用户浏览器
    #return render(request,"something.html",{"title":"来了"})

    #   6.【响应】重定向到其他页面
    return redirect("https://www.baidu.com")


def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        #   如果是POST请求，则获取用户输入内容
        print(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('password')

        if username == 'sunrise' and password == '9425':
            return redirect("https://www.baidu.com")
        else:
            #return HttpResponse("登录失败")
            return render(request, 'login.html',{"error_msg":"用户名或密码错误"})


def orm_test(request):
    # UserInfo.objects.create(name='sunrise', password='9425', age=18)
    # UserInfo.objects.create(name='ole', password='777', age=5)
    # UserInfo.objects.create(name='queen', password='390', age=28)
    return HttpResponse('数据已处理～')


def person_management(request):
    # 获取数据库表中的所有数据
    datalist = UserInfo.objects.all()
    # 渲染后返回给浏览器
    return render(request,'person_management.html',{'datalist':datalist})


def person_add(request):
    if request.method == 'GET':
        return render(request, 'person_add.html')

    # 获取用户提交的数据
    username = request.POST.get('username')
    password = request.POST.get('password')
    age = request.POST.get('age')

    # 添加到数据库
    UserInfo.objects.create(name=username, password=password, age=age)
    return redirect('/person/management/')


def person_delete(request):
    d_id = request.GET.get('id')
    UserInfo.objects.filter(id=d_id).delete()
    return redirect('/person/management/')