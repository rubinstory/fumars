# Generated by Django 3.0.8 on 2020-07-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200726_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accounts',
            name='type',
            field=models.CharField(choices=[('temp', '승인 대기중'), ('user', '사용자'), ('admin', '관리자')], default='', max_length=20),
        ),
    ]
