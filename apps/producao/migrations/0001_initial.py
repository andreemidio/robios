# Generated by Django 3.2.9 on 2021-11-25 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line', models.IntegerField(null=True)),
                ('datetime_turn', models.DateTimeField(auto_now_add=True)),
                ('parts_quantity', models.IntegerField()),
                ('area_production', models.FloatField()),
                ('line_stops', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Producao',
                'verbose_name_plural': 'Producoes',
                'db_table': 'producao',
            },
        ),
        migrations.CreateModel(
            name='Quantity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateTimeField(null=True)),
                ('fim', models.DateTimeField(null=True)),
                ('producao', models.ManyToManyField(null=True, to='producao.Producao')),
            ],
            options={
                'verbose_name': 'quantity',
                'verbose_name_plural': 'quantities',
                'db_table': 'quantity',
            },
        ),
    ]
