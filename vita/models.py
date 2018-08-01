
from django.db import models

# Create your models here.
from django.db import models
from django.db.models import DateTimeField
from django.utils import timezone


class User(models.Model):
    nick_name = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=11)
    pub_date: DateTimeField = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.nick_name

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - timezone.timedelta(days=20)


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    birth_date = models.DateTimeField('User Birthday Date')
    contact_address = models.CharField(max_length=100)

    def __str__(self):
        return self.contact_address
