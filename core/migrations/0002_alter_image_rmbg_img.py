# Generated by Django 4.2 on 2023-04-10 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='rmbg_img',
            field=models.ImageField(blank=True, upload_to='rmbg_img/'),
        ),
    ]
