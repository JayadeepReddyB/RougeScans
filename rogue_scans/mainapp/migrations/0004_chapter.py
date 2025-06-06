# Generated by Django 5.1.6 on 2025-03-11 10:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_manga_desc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('chapter_number', models.PositiveBigIntegerField()),
                ('release_date', models.DateField()),
                ('manga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.manga')),
            ],
        ),
    ]
