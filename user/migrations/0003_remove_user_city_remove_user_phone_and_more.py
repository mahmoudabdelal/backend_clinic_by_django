# Generated by Django 4.1.2 on 2023-01-31 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='City',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Phone',
        ),
        migrations.RemoveField(
            model_name='user',
            name='Street',
        ),
    ]
