# Generated by Django 3.2.4 on 2021-07-06 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_bloguser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Bloguser',
        ),
    ]