# Generated by Django 3.0.7 on 2020-07-01 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_store', '0004_auto_20200630_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photographer',
            name='bio',
            field=models.TextField(blank=True, default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photographer',
            name='home',
            field=models.CharField(blank=True, default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photographer',
            name='instaHandle',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photographer',
            name='instituition',
            field=models.CharField(blank=True, default=' ', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='photographer',
            name='profile_pic',
            field=models.URLField(null=True),
        ),
    ]
