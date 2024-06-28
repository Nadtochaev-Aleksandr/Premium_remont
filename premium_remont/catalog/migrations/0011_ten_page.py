# Generated by Django 5.0.4 on 2024-06-11 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_alter_eighth_page_p8image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ten_page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p10_img', models.ImageField(default='img', upload_to='catalog/img/')),
                ('p10_title', models.CharField(max_length=250)),
                ('p10_content', models.CharField(max_length=250)),
            ],
        ),
    ]
