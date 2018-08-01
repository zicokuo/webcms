# 简历路由

from django.urls import path
# 引入视图
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]
