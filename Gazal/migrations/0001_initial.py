# Generated by Django 4.0.3 on 2022-03-13 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auditoriya_yoshi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yosh', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gazal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=200)),
                ('auditoriya_yoshi', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gazal.auditoriya_yoshi')),
            ],
        ),
        migrations.CreateModel(
            name='Matn_tipi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Misra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('misra', models.CharField(max_length=200)),
                ('gazal_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gazal.gazal')),
            ],
        ),
        migrations.CreateModel(
            name='Soz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('soz', models.CharField(blank=True, max_length=100)),
                ('mano', models.CharField(blank=True, max_length=100)),
                ('janr', models.CharField(default='g`azal', max_length=100)),
                ('satr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gazal.misra')),
                ('soz_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Gazal.gazal')),
                ('tip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gazal.matn_tipi')),
                ('yosh', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gazal.auditoriya_yoshi')),
            ],
        ),
        migrations.AddField(
            model_name='gazal',
            name='matn_tipi',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Gazal.matn_tipi'),
        ),
    ]
