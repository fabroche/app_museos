# Generated by Django 4.2.1 on 2023-05-30 05:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exposicion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=255)),
                ('hora_apertura', models.DateTimeField()),
                ('hora_clausura', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Museo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('descripcion', models.TextField(blank=True)),
                ('exposiciones', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museo.exposicion')),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='museo.horario')),
            ],
        ),
    ]
