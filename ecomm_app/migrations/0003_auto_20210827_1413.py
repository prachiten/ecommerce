# Generated by Django 2.2 on 2021-08-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecomm_app', '0002_auto_20210827_1324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
