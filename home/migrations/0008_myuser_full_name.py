# Generated by Django 3.2.4 on 2021-07-07 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_myuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='full_name',
            field=models.CharField(default='Admin', max_length=100),
            preserve_default=False,
        ),
    ]