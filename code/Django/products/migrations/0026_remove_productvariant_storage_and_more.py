# Generated by Django 4.0.4 on 2022-05-19 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_brand_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productvariant',
            name='storage',
        ),
        migrations.AlterField(
            model_name='productvariant',
            name='colour',
            field=models.CharField(max_length=100),
        ),
        migrations.CreateModel(
            name='ProductStorages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storage', models.IntegerField()),
                ('product_variant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_variant_storages', to='products.productvariant')),
            ],
        ),
    ]
