# Generated by Django 5.1.6 on 2025-03-26 04:53

import django.db.models.deletion
import mainapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0004_chapter'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChapterImage',
            fields=[
                ('id', models.PositiveBigIntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to=mainapp.models.chapter_image_upload_path)),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.chapter')),
            ],
        ),
    ]
