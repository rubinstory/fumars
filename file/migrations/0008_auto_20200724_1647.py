# Generated by Django 3.0.8 on 2020-07-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0007_auto_20200724_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='file_name',
        ),
        migrations.AddField(
            model_name='file',
            name='subject',
            field=models.CharField(default='컴퓨터시스템입문', help_text='줄임말이 아닌 수업명 입력', max_length=200),
        ),
    ]
