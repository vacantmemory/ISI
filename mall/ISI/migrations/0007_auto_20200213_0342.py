# Generated by Django 3.0.3 on 2020-02-13 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISI', '0006_auto_20200213_0229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail_image',
            field=models.CharField(max_length=15),
        ),
    ]