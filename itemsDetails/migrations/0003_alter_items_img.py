# Generated by Django 4.2.3 on 2023-07-22 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemsDetails', '0002_items_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='img',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]