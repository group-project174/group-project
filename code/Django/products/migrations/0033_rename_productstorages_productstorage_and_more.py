# Generated by Django 4.0.4 on 2022-05-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0032_productvariant_unique_variant'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ProductStorages',
            new_name='ProductStorage',
        ),
        migrations.AlterField(
            model_name='product',
            name='specifications',
            field=models.CharField(blank=True, default='', max_length=2000),
        ),
    ]
