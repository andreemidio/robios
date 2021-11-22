# Generated by Django 3.2.9 on 2021-11-21 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nome_sobrenome', models.CharField(blank=True, max_length=255, null=True)),
                ('cpf', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('reset_password', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(blank=True, default=False, null=True)),
                ('is_staff', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'Usuarios',
                'ordering': ['-data_criacao'],
            },
        ),
    ]
