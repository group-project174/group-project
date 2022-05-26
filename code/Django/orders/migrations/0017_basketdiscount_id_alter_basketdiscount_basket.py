# Generated by Django 4.0.4 on 2022-05-16 22:04

import annoying.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_remove_basketdiscount_id_alter_basketdiscount_basket'),
    ]

    operations = [
        # migrations.AddField(
        #     model_name='basketdiscount',
        #     name='id',
        #     field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        #     preserve_default=False,
        # ),
        migrations.AlterField(
            model_name='basketdiscount',
            name='basket',
            field=annoying.fields.AutoOneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basket_discount', to='orders.basket'),
        ),
    ]