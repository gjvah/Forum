# Generated by Django 2.2 on 2019-12-09 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0007_auto_20191208_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='style',
            field=models.CharField(max_length=45),
        ),
    ]
