# Generated by Django 3.0.5 on 2021-05-20 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0005_auto_20210521_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='usr_pic',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
