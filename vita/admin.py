from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

# 向django管理后台注册用户数据model管理
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(PostKind)
admin.site.register(Category)
