# Generated by Django 2.1 on 2018-08-02 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vita', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind_text', models.CharField(max_length=40)),
                ('kind_name_text', models.CharField(max_length=60)),
                ('template_text', models.TextField(default='')),
            ],
        ),
    ]
