# Generated by Django 2.1.4 on 2018-12-06 12:37

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章正文'),
        ),
    ]
