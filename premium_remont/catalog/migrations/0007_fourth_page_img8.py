# Generated by Django 5.0.4 on 2024-06-11 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_eighth_page_p8image'),
    ]

    operations = [
        migrations.AddField(
            model_name='fourth_page',
            name='img8',
            field=models.ImageField(default='img', upload_to=''),
        ),
    ]
