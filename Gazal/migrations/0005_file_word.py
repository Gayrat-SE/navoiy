# Generated by Django 4.0.3 on 2022-03-26 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gazal', '0004_file_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='File_Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('files', models.FileField(blank=True, upload_to='files')),
            ],
        ),
    ]
