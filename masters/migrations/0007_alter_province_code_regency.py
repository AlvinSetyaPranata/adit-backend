# Generated by Django 5.1.4 on 2025-03-11 04:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('masters', '0006_alter_province_meta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.CharField(max_length=10, unique=True),
        ),
        migrations.CreateModel(
            name='Regency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('province', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='regencies', to='masters.province')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
