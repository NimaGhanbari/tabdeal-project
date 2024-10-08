# Generated by Django 4.2 on 2024-09-02 13:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("charge", "0002_alter_creditrequest_seller_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="creditrequest",
            name="seller_profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="credit_request",
                to="charge.sellerprofile",
            ),
        ),
    ]
