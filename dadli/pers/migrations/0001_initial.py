# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-18 19:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('social_django', '0006_partial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Catobj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Cats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_az', models.CharField(default='NULL', max_length=50)),
                ('cat_en', models.CharField(default='NULL', max_length=50)),
                ('cat_ru', models.CharField(default='NULL', max_length=50)),
                ('cat_tr', models.CharField(default='NULL', max_length=50)),
                ('cat_ar', models.CharField(default='NULL', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Objinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objt', models.CharField(max_length=250)),
                ('adres', models.CharField(default='NULL', max_length=250)),
                ('erazi', models.CharField(default='NULL', max_length=250)),
                ('metro', models.CharField(default='NULL', max_length=250)),
                ('city_reg', models.CharField(default='NULL', max_length=250)),
                ('city', models.CharField(default='NULL', max_length=250)),
                ('country', models.CharField(default='NULL', max_length=250)),
                ('zip', models.CharField(default='AZ0000', max_length=10)),
                ('fammeal', models.CharField(default='NULL', max_length=100)),
                ('menu', models.CharField(default='NULL', max_length=5000)),
                ('delivery', models.BooleanField(default=False)),
                ('tel1', models.CharField(default='NULL', max_length=14)),
                ('tel2', models.CharField(default='NULL', max_length=14)),
                ('tel3', models.CharField(default='NULL', max_length=14)),
                ('mob1', models.CharField(default='NULL', max_length=14)),
                ('mob2', models.CharField(default='NULL', max_length=14)),
                ('mob3', models.CharField(default='NULL', max_length=14)),
                ('mob4', models.CharField(default='NULL', max_length=14)),
                ('mob5', models.CharField(default='NULL', max_length=14)),
                ('info', models.TextField(default='NULL', max_length=5000)),
                ('pic0', models.URLField(default='NULL', max_length=1000)),
                ('pic1', models.URLField(default='NULL', max_length=1000)),
                ('pic2', models.URLField(default='NULL', max_length=1000)),
                ('pic3', models.URLField(default='NULL', max_length=1000)),
                ('pic4', models.URLField(default='NULL', max_length=1000)),
                ('pic5', models.URLField(default='NULL', max_length=1000)),
                ('pic6', models.URLField(default='NULL', max_length=1000)),
                ('pic7', models.URLField(default='NULL', max_length=1000)),
                ('pic8', models.URLField(default='NULL', max_length=1000)),
                ('pic9', models.URLField(default='NULL', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Tagobj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('objid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pers.Objinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagaz', models.CharField(default='NULL', max_length=100)),
                ('tagru', models.CharField(default='NULL', max_length=100)),
                ('tagen', models.CharField(default='NULL', max_length=100)),
                ('tagtr', models.CharField(default='NULL', max_length=100)),
                ('tagar', models.CharField(default='NULL', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Ustags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pers.Objinfo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='social_django.UserSocialAuth')),
            ],
        ),
        migrations.AddField(
            model_name='tagobj',
            name='tagid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pers.Tags'),
        ),
        migrations.AddField(
            model_name='catobj',
            name='catid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pers.Cats'),
        ),
        migrations.AddField(
            model_name='catobj',
            name='objid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pers.Objinfo'),
        ),
    ]
