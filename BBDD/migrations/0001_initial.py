# Generated by Django 3.1.5 on 2021-07-23 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Matricula', models.CharField(max_length=150)),
                ('Nombre', models.CharField(max_length=150)),
                ('ApellidoPaterno', models.CharField(max_length=150)),
                ('ApellidoMaterno', models.CharField(max_length=150)),
                ('Correo', models.EmailField(max_length=254)),
                ('Telefono', models.CharField(max_length=10)),
                ('TipoPerido', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Alumno',
                'verbose_name_plural': 'Alumnos',
            },
        ),
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField()),
                ('Cuatrimestral', models.BooleanField()),
                ('NumCuatrimestres', models.IntegerField(default=0)),
                ('Semestral', models.BooleanField()),
                ('NumSemestres', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=50)),
                ('Cantidad', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'TipoPago',
                'verbose_name_plural': 'TipoPagos',
            },
        ),
        migrations.CreateModel(
            name='HistPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pagado', models.BooleanField()),
                ('Alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBDD.alumno')),
                ('Pago', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='BBDD.tipopago')),
            ],
            options={
                'verbose_name': 'HistPago',
                'verbose_name_plural': 'HistPagos',
            },
        ),
        migrations.AddField(
            model_name='alumno',
            name='Carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BBDD.carrera'),
        ),
    ]
