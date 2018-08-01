from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import User as UserModel


def index(request):
    userList = UserModel.objects.all()[0:10]
    context = {'userVitaList': userList}
    return render(request, 'vita/userVita.html', context)


def post(request, post_id):
    response = "您正在浏览 %s 的内容页"
    return HttpResponse(response % post_id)


def userVita(request, user_id):
    print(user_id)
    user = UserModel.objects.filter(id=user_id).get()
    response = "您正在浏览 %s 的个人信息" + user.nick_name
    return HttpResponse(response % user_id)
