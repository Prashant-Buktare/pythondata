# Generated by Django 2.1.1 on 2018-11-30 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0006_auto_20181130_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profileimage',
            field=models.ImageField(blank=True, null=True, upload_to='Profile_images'),
        ),
    ]
