# Generated by Django 4.1 on 2022-10-01 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_alter_orderitem_order_alter_orderitem_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='stripe_token',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
