# Generated by Django 5.1.7 on 2025-04-04 22:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masters', '0020_income'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('nik', models.CharField(max_length=16)),
                ('kk', models.CharField(max_length=16)),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=15)),
                ('income', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='masters.income')),
                ('job', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='masters.job')),
            ],
            options={
                'ordering': ['first_name'],
            },
        ),
    ]
