# Generated by Django 2.2.3 on 2019-07-07 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ORM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='type',
            field=models.CharField(choices=[(1, '实战课'), (2, '免费课'), (0, '其他')], default=0, max_length=1, verbose_name='课程类型'),
        ),
    ]