# Generated by Django 4.0.3 on 2022-03-12 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Devon', '0002_alter_devon_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Janrlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('devon_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Devon.devon')),
            ],
        ),
    ]
