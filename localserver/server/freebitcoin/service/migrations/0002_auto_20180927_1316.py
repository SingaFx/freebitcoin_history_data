# Generated by Django 2.2 on 2018-09-27 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bet',
            name='balance_after',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AddField(
            model_name='bet',
            name='balance_before',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
