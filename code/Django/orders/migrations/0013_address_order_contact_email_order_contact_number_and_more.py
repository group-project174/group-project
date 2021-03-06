# Generated by Django 4.0.4 on 2022-05-14 21:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_remove_specification_non_fungible_spec_product_pairs_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('orders', '0012_remove_basketproduct_product_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('house_number', models.IntegerField(null=True)),
                ('first_line', models.CharField(max_length=100)),
                ('second_line', models.CharField(max_length=100, null=True)),
                ('post_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='contact_email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='contact_number',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discount_orders', to='products.discount'),
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='order_total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='order',
            name='savings',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_orders', to='products.productvariant'),
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=16)),
                ('expiry_date', models.DateField()),
                ('security_code', models.CharField(max_length=3)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_cards', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address_orders', to='orders.address'),
        ),
        migrations.AddField(
            model_name='order',
            name='card',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='card_orders', to='orders.card'),
        ),
    ]
