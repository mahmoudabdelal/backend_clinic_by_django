# Generated by Django 4.1.2 on 2023-02-01 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consulation', '0002_alter_consulation_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consulation',
            name='Doctor_id',
        ),
        migrations.RemoveField(
            model_name='consulation',
            name='Patient_id',
        ),
    ]
