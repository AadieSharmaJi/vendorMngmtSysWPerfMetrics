# Generated by Django 4.2.7 on 2023-12-04 09:24

from django.db import migrations, models
import vendorProfileMngmnt.models


class Migration(migrations.Migration):

    dependencies = [
        ('vendorProfileMngmnt', '0002_alter_vendor_vendor_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(default=0, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(default=0, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(default=0, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(default=0, editable=False, max_length=20),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='vendor_code',
            field=models.CharField(default=vendorProfileMngmnt.models.incremental_vendor_id, editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
