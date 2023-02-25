# Generated by Django 4.1.6 on 2023-02-24 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=150, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(db_index=True, max_length=150, unique=True, verbose_name='Ссылка'),
        ),
    ]