# Generated by Django 3.0.8 on 2020-07-26 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20200726_1516'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounts',
            old_name='type',
            new_name='access_type',
        ),
    ]
