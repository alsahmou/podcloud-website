# Generated by Django 2.0.7 on 2019-11-12 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0010_auto_20191112_0226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='podcast_image',
            field=models.ImageField(blank=True, default='Mic.png', null=True, upload_to=''),
        ),
    ]