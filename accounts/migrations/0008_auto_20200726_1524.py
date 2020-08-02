# Generated by Django 3.0.8 on 2020-07-26 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200726_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='access_type',
            field=models.CharField(choices=[('temp', '승인 대기중'), ('user', '사용자'), ('admin', '관리자')], default=('temp', '승인 대기중'), max_length=20),
        ),
    ]