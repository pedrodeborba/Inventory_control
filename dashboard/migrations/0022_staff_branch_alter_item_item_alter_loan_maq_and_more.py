# Generated by Django 5.0.7 on 2024-12-10 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_remove_loan_equipment'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='branch',
            field=models.CharField(choices=[('Matriz (01)', 'Matriz (01)'), ('Parobé (04)', 'Parobé (04)'), ('Campo Bom (11)', 'Campo Bom (11)'), ('Dois Irmãos (03 - 05)', 'Dois Irmãos (03 - 05)'), ('São Paulo (02)', 'São Paulo (02)')], default=1, max_length=50, verbose_name='Filial'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='item',
            name='item',
            field=models.CharField(max_length=100, verbose_name='Item'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='maq',
            field=models.IntegerField(blank=True, null=True, verbose_name='MAQ'),
        ),
        migrations.AlterField(
            model_name='loan',
            name='patrimony',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True, verbose_name='Patrimônio'),
        ),
        migrations.AlterField(
            model_name='order',
            name='branch',
            field=models.CharField(choices=[('Matriz (01)', 'Matriz (01)'), ('Parobé (04)', 'Parobé (04)'), ('Campo Bom (11)', 'Campo Bom (11)'), ('Dois Irmãos (03 - 05)', 'Dois Irmãos (03 - 05)'), ('São Paulo (02)', 'São Paulo (02)')], max_length=50, verbose_name='Filial'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='order',
            name='information',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Informação Adicional'),
        ),
        migrations.AlterField(
            model_name='order',
            name='maq',
            field=models.IntegerField(blank=True, null=True, verbose_name='MAQ'),
        ),
        migrations.AlterField(
            model_name='order',
            name='movimentation',
            field=models.CharField(choices=[('E', 'Entrada'), ('S', 'Saída')], max_length=1, verbose_name='Movimentação'),
        ),
        migrations.AlterField(
            model_name='order',
            name='num_called',
            field=models.IntegerField(verbose_name='Chamado'),
        ),
        migrations.AlterField(
            model_name='order',
            name='patrimony',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True, verbose_name='Patrimônio'),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Setor'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='badge',
            field=models.IntegerField(null=True, unique=True, verbose_name='Crachá'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='ranking',
            field=models.CharField(max_length=100, null=True, verbose_name='Cargo'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='username',
            field=models.CharField(max_length=100, null=True, verbose_name='Nome de Usuário'),
        ),
    ]