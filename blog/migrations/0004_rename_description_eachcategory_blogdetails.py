# Generated by Django 3.2.8 on 2022-02-01 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_eachcategory_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eachcategory',
            old_name='Description',
            new_name='Blogdetails',
        ),
    ]
