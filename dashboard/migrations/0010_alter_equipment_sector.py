# Generated by Django 5.0.7 on 2024-07-26 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_rename_category_item_alter_item_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipment',
            name='sector',
            field=models.ForeignKey(default='ESTOQUE TI', null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.sector'),
        ),
    ]