# Generated by Django 2.1.3 on 2019-04-21 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lifeapp', '0003_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='introduction',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
