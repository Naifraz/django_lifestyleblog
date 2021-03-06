# Generated by Django 2.1.3 on 2019-05-27 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lifeapp', '0009_auto_20190527_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='height_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='article',
            name='width_field',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to='', width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='article',
            name='introduction',
            field=models.TextField(max_length=100),
        ),
    ]
