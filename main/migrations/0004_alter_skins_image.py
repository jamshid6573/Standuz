# Generated by Django 4.0.6 on 2022-08-01 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_skins_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skins',
            name='image',
            field=models.ImageField(default=None, upload_to='SKINS/'),
        ),
    ]
