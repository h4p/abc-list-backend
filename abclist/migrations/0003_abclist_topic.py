# Generated by Django 3.2.4 on 2021-07-03 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('abclist', '0002_alter_abclist_abclist'),
    ]

    operations = [
        migrations.AddField(
            model_name='abclist',
            name='topic',
            field=models.CharField(default='', max_length=255),
        ),
    ]
