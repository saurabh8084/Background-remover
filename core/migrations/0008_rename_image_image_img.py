# Generated by Django 4.2 on 2023-04-10 10:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_rename_img_image_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='image',
            new_name='img',
        ),
    ]
