# Generated by Django 4.2.7 on 2023-11-15 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsletters', '0007_alter_client_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='owner',
            new_name='author',
        ),
    ]
