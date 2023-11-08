# Generated by Django 4.2.4 on 2023-11-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_laptop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='brand',
            field=models.CharField(choices=[('Asus', 'Asus'), ('Acer', 'Acer'), ('Apple', 'Apple'), ('Lenovo', 'Lenovo'), ('Dell', 'Dell')], max_length=6),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='operation_system',
            field=models.CharField(choices=[('Windows', 'Windows'), ('MacOS', 'MacOS'), ('Linux', 'Linux'), ('Chrome OS', 'Chrome OS')], max_length=9),
        ),
    ]
