# Generated by Django 2.1 on 2018-08-01 15:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birth_date', models.DateTimeField(verbose_name='User Birthday Date')),
                ('contact_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login_account', models.CharField(max_length=60)),
                ('login_password', models.CharField(max_length=20)),
                ('nick_name', models.CharField(max_length=20)),
                ('contact_phone', models.CharField(max_length=11)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vita.User'),
        ),
    ]