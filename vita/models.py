from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# 基本用户信息
class User(models.Model):
    nick_name = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=11)
    pub_date = models.DateTimeField('User publish date')

    def __str__(self):
        return self.nick_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=20)


# 详细用户信息
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateTimeField('User Birthday Date')
    contact_address = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_address


# 文章信息
class Post(models.Model):
    # kind = models.ForeignKey(Kind, on_delete=models.CASCADE, default=0)
    title_text = models.CharField(max_length=120)
    content_text = models.TextField(default='')
    pub_date = models.DateTimeField('post publish date')
    update_date = models.DateTimeField('post update date')
    cate_id = models.IntegerField(default=0)

    def __str__(self):
        return self.title_text


# 文章类型
class PostKind(models.Model):
    kind_text = models.CharField(max_length=40)
    kind_name_text = models.CharField(max_length=60)
    template_text = models.TextField(default='')

    def __str__(self):
        return self.kind_text

    # 文章分类


class Category(models.Model):
    cate_title_text = models.CharField(max_length=60)
    cate_name_text = models.CharField(max_length=100)
    parent_id_int = models.IntegerField(default=0)

    def __str__(self):
        return self.cate_title_text
