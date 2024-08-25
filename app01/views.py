from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    return HttpResponse(' 欢迎使用 ')


def user_list(request):
    return render(request, 'user_list.html')


def user_add(request):
    return render(request, 'user_add.html')


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