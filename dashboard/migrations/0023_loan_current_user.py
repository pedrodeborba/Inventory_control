# Generated by Django 5.0.7 on 2024-12-10 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0022_staff_branch_alter_item_item_alter_loan_maq_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan',
            name='current_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='current_loan', to='dashboard.staff'),
        ),
    ]