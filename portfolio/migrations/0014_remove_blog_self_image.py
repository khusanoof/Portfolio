# Generated by Django 5.1.3 on 2024-11-30 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_blog_self_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='self_image',
        ),
    ]