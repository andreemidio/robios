# Generated by Django 3.2.11 on 2022-01-23 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0002_alter_quantity_producao'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParadasProducao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]