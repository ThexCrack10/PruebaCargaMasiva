# Generated by Django 2.1.1 on 2018-09-21 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caracteristica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CaracteristicaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.TextField()),
                ('caracteristica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Caracteristica')),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CodigoProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Comercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='MedidaProducto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caracteristicas', models.ManyToManyField(through='backend.CaracteristicaProducto', to='backend.Caracteristica')),
                ('categorias', models.ManyToManyField(to='backend.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='RubroComercio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='TipoCodigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UnidadDeMedida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='codigos',
            field=models.ManyToManyField(through='backend.CodigoProducto', to='backend.TipoCodigo'),
        ),
        migrations.AddField(
            model_name='producto',
            name='comercios',
            field=models.ManyToManyField(to='backend.Comercio'),
        ),
        migrations.AddField(
            model_name='producto',
            name='medidas',
            field=models.ManyToManyField(through='backend.MedidaProducto', to='backend.UnidadDeMedida'),
        ),
        migrations.AddField(
            model_name='medidaproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Producto'),
        ),
        migrations.AddField(
            model_name='medidaproducto',
            name='unidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.UnidadDeMedida'),
        ),
        migrations.AddField(
            model_name='comercio',
            name='rubro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.RubroComercio'),
        ),
        migrations.AddField(
            model_name='codigoproducto',
            name='codigo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.TipoCodigo'),
        ),
        migrations.AddField(
            model_name='codigoproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Producto'),
        ),
        migrations.AddField(
            model_name='caracteristicaproducto',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Producto'),
        ),
    ]