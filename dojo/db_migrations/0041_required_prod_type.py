# Generated by Django 2.2.12 on 2020-05-17 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0040_finding_cwe_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prod_type', to='dojo.Product_Type'),
        ),
    ]
