# Generated by Django 3.2.8 on 2022-01-31 20:26

import blog.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='EachCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=250)),
                ('Title', models.CharField(default='', max_length=250)),
                ('Description', models.CharField(default='', max_length=250)),
                ('Image', models.ImageField(blank=True, default='posts/default.png', upload_to=blog.models.upload_location, verbose_name='Image')),
                ('start_date', models.DateField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.allcategory')),
            ],
            options={
                'ordering': ('Name',),
            },
        ),
    ]
