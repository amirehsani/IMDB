# Generated by Django 4.1.3 on 2022-11-22 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviecomment',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='moviecomment',
            name='parent_comment',
        ),
        migrations.RemoveField(
            model_name='moviecomment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='moviecomment',
            name='validated_by',
        ),
        migrations.DeleteModel(
            name='CrewComment',
        ),
        migrations.DeleteModel(
            name='MovieComment',
        ),
    ]
