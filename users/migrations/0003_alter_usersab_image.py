# Generated by Django 4.0.6 on 2022-07-24 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersab_image_alter_usersab_gold'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersab',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
