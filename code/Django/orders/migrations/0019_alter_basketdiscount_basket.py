# Generated by Django 4.0.4 on 2022-05-16 22:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_alter_basketdiscount_basket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basketdiscount',
            name='basket',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='basket_discount', to='orders.basket'),
        ),
    ]