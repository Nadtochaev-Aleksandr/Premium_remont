# Generated by Django 5.0.4 on 2024-06-10 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_eighth_page_alter_fourth_page_list_text_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eighth_page',
            name='p8image',
            field=models.FileField(upload_to=''),
        ),
    ]
