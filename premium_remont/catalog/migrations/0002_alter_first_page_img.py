# Generated by Django 5.0.4 on 2024-05-09 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first_page',
            name='img',
            field=models.FileField(default='img', upload_to='catalog/img/'),
        ),
    ]
