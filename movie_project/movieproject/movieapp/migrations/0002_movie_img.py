# Generated by Django 4.1.4 on 2023-01-06 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='img',
            field=models.ImageField(default=int, upload_to='pics'),
            preserve_default=False,
        ),
    ]