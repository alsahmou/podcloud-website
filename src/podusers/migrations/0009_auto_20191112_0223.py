# Generated by Django 2.0.7 on 2019-11-12 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0008_auto_20191112_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poduser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='profilepicture.jpeg', null=True, upload_to=''),
        ),
    ]
