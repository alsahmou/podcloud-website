# Generated by Django 2.0.7 on 2019-11-09 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('podusers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='poduser',
            name='trial',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]