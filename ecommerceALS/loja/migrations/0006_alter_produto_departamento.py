# Generated by Django 5.1.7 on 2025-03-22 22:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0005_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='departamento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='produtos', to='loja.departamento'),
        ),
    ]
