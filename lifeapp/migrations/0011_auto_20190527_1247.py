# Generated by Django 2.1.3 on 2019-05-27 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeapp', '0010_auto_20190527_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='height_field',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='article',
            name='width_field',
            field=models.IntegerField(default=100),
        ),
    ]
