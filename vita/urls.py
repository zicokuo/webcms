# 简历路由

from django.urls import path
# 引入视图
from . import views

urlpatterns = [
    # index主页
    path('', views.index, name="index"),
    # post文章页
    path('<int:user_id>/', views.userVita, name='postDetails')
]
