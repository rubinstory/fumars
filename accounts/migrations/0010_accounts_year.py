# Generated by Django 3.0.8 on 2020-07-27 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200726_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='year',
            field=models.CharField(default='0000', help_text='입학년도를 4자리로 입력', max_length=4),
        ),
    ]
