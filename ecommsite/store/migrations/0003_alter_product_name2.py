# Generated by Django 3.2.5 on 2021-09-19 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_alter_product_name2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name2',
            field=models.CharField(max_length=100),
        ),
    ]
