# Generated by Django 5.0.6 on 2024-07-05 17:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_equipment_maq_alter_equipment_patrimony'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipment',
            name='quantity',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='maq',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='patrimony',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_called', models.IntegerField()),
                ('order_quantity', models.PositiveIntegerField(null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('equipment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dashboard.equipment')),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]