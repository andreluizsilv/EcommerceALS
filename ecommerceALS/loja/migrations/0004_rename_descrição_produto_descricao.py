# Generated by Django 5.1.7 on 2025-03-16 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_descrição_produto_unidade'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='descrição',
            new_name='descricao',
        ),
    ]
