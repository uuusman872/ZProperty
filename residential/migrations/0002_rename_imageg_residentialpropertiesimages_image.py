# Generated by Django 3.2.7 on 2021-10-15 09:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('residential', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='residentialpropertiesimages',
            old_name='imageg',
            new_name='Image',
        ),
    ]
