# Generated by Django 3.0.5 on 2021-05-08 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_auto_20210508_2348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='numb_of_subs',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='price1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='price2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='price3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='slug',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
