# Generated by Django 4.1.2 on 2023-02-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_alter_reservation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='Doctor_ID',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='Patient_ID',
        ),
    ]
