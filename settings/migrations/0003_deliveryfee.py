# Generated by Django 4.2.5 on 2023-10-30 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0002_rename_call_as_company_call_us_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeliveryFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fee', models.FloatField()),
            ],
        ),
    ]
