# Generated by Django 5.0.7 on 2024-09-04 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_order_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=99, verbose_name='Título')),
                ('subtitle', models.CharField(blank=True, max_length=99, verbose_name='Subtítulo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='cards/images/', verbose_name='Imagem')),
                ('link', models.CharField(blank=True, max_length=255, null=True, verbose_name='Levar para')),
            ],
        ),
    ]