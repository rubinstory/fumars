# Generated by Django 3.0.8 on 2020-08-05 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200805_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='accounts',
            name='major',
            field=models.CharField(choices=[('eec', '전자'), ('ece', '전기'), ('cse', '컴퓨터')], default='', max_length=20),
        ),
    ]