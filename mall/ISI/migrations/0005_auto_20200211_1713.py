# Generated by Django 3.0.3 on 2020-02-11 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ISI', '0004_auto_20200211_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='thumbnail_image',
            field=models.BinaryField(),
        ),
    ]
