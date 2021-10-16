# Generated by Django 3.2.7 on 2021-10-15 09:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RedsidentialProperties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('overview', models.TextField()),
                ('Price', models.CharField(max_length=100)),
                ('Area', models.CharField(max_length=100)),
                ('Location', models.CharField(max_length=100)),
                ('num_bedRooms', models.CharField(max_length=100)),
                ('num_WashRooms', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentialPropertiesImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('imageg', models.ImageField(upload_to='Media/ResidentialInvesment/Gallery')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='residential.redsidentialproperties')),
            ],
        ),
    ]
