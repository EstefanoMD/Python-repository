# Generated by Django 4.1.3 on 2022-12-20 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='categoria',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Contato',
        ),
    ]
