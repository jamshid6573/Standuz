# Generated by Django 4.0.6 on 2023-05-21 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_usersab_total_gold_alter_usersab_gold'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersab',
            name='is_ban',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usersab',
            name='number',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='usersab',
            name='open_box',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usersab',
            name='role',
            field=models.CharField(blank=True, choices=[('user', 'user'), ('admin', 'admin'), ('youtuber', 'youtuber')], default='user', max_length=255),
        ),
        migrations.AddField(
            model_name='usersab',
            name='sum',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='usersab',
            name='tg',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
