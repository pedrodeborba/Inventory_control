# Generated by Django 5.0.7 on 2024-09-05 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to='profile_pics'),
        ),
    ]
