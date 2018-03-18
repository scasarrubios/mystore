# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bike',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='book',
            name='argument',
        ),
        migrations.RemoveField(
            model_name='book',
            name='prize',
        ),
        migrations.RemoveField(
            model_name='cd',
            name='prize',
        ),
        migrations.AddField(
            model_name='bike',
            name='price',
            field=models.FloatField(default=149.99),
        ),
        migrations.AddField(
            model_name='book',
            name='price',
            field=models.FloatField(default=15),
        ),
        migrations.AddField(
            model_name='book',
            name='style',
            field=models.CharField(default=b'Aventuras', max_length=400),
        ),
        migrations.AddField(
            model_name='cd',
            name='price',
            field=models.FloatField(default=15),
        ),
        migrations.AlterField(
            model_name='bike',
            name='characts',
            field=models.CharField(default=b'Color: Negro \n', max_length=600),
        ),
        migrations.AlterField(
            model_name='bike',
            name='img',
            field=models.CharField(default=b'thunderbolt.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='bike',
            name='name',
            field=models.CharField(default=b'Bici', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default=b'Dan Brown', max_length=70),
        ),
        migrations.AlterField(
            model_name='book',
            name='img',
            field=models.CharField(default=b'danbrown.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(default=b'El Codigo Da Vinci', max_length=50),
        ),
        migrations.AlterField(
            model_name='cd',
            name='author',
            field=models.CharField(default=b'Queen', max_length=70),
        ),
        migrations.AlterField(
            model_name='cd',
            name='img',
            field=models.CharField(default=b'queen.jpg', max_length=200),
        ),
        migrations.AlterField(
            model_name='cd',
            name='style',
            field=models.CharField(default=b'Rock', max_length=30),
        ),
        migrations.AlterField(
            model_name='cd',
            name='title',
            field=models.CharField(default=b'Jazz', max_length=50),
        ),
    ]
