# Generated by Django 4.1 on 2022-11-01 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='body',
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(blank=True),
        ),
    ]