# Generated by Django 3.2.9 on 2021-11-21 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quantity',
            name='fim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='inicio',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='quantity',
            name='resultado',
            field=models.DateTimeField(null=True),
        ),
    ]
