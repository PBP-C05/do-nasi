# Generated by Django 4.1 on 2022-10-28 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harapan_page', '0003_remove_harapandonatur_harapan_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='harapandonatur',
            name='username',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
