# Generated by Django 4.2.1 on 2023-06-03 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_usersab_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersab',
            name='sum',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
