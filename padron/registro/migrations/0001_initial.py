# Generated by Django 2.1.4 on 2018-12-18 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Canton',
            fields=[
                ('codigo', models.SmallIntegerField(default=0, max_length=2, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=20, verbose_name='Canton')),
            ],
            options={
                'verbose_name': 'Canton',
                'verbose_name_plural': 'Cantones',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Codigo_Electoral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Codigo electoral',
                'verbose_name_plural': 'Codigos electorales',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Distrito',
            fields=[
                ('codigo', models.SmallIntegerField(default=0, max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=34, verbose_name='Distrito')),
            ],
            options={
                'verbose_name': 'Distrito',
                'verbose_name_plural': 'Distritos',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('cedula', models.TextField(max_length=9, primary_key=True, serialize=False, verbose_name='Cedula')),
                ('sexo', models.TextField(max_length=9, verbose_name='Sexo')),
                ('codigo_electoral', models.SmallIntegerField(default=0, max_length=6)),
                ('fecha_nacimiento', models.DateTimeField()),
                ('junta', models.SmallIntegerField(default=0, max_length=5)),
                ('nombre', models.TextField(max_length=30, verbose_name='Nombre')),
                ('apellido_1', models.TextField(max_length=26, verbose_name='Apellido1')),
                ('apellido_2', models.TextField(max_length=26, verbose_name='Apellido2')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='Provincia',
            fields=[
                ('codigo', models.SmallIntegerField(default=0, max_length=1, primary_key=True, serialize=False)),
                ('nombre', models.TextField(max_length=10, verbose_name='Provincia')),
            ],
            options={
                'verbose_name': 'Provincia',
                'verbose_name_plural': 'Provincias',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroSexo',
            fields=[
                ('sexo', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro de sexo',
                'verbose_name_plural': 'Registros de sexo',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroVencimiento',
            fields=[
                ('vencimiento', models.DateField(default=0, primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Vencimiento',
                'verbose_name_plural': 'Vencimientos',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroCanton',
            fields=[
                ('canton', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registro.Canton')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro de canton',
                'verbose_name_plural': 'Registros de canton',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroCodigoElectoral',
            fields=[
                ('codigo_electoral', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registro.Codigo_Electoral')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro de codigo electoral',
                'verbose_name_plural': 'Registros de codigos electorales',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroDistrito',
            fields=[
                ('distrito', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registro.Distrito')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro de distrito',
                'verbose_name_plural': 'Registros de distrito',
                'ordering': ('pk',),
            },
        ),
        migrations.CreateModel(
            name='RegistroProvincia',
            fields=[
                ('provincia', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='registro.Provincia')),
                ('cantidad', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Registro de provincia',
                'verbose_name_plural': 'Registros de provincia',
                'ordering': ('pk',),
            },
        ),
        migrations.AddField(
            model_name='codigo_electoral',
            name='canton',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Canton'),
        ),
        migrations.AddField(
            model_name='codigo_electoral',
            name='distrito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Distrito'),
        ),
        migrations.AddField(
            model_name='codigo_electoral',
            name='provincia',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='registro.Provincia'),
        ),
    ]
