# Generated by Django 5.1.4 on 2024-12-30 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
