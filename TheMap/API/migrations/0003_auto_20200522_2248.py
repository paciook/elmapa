# Generated by Django 3.0.5 on 2020-05-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_auto_20200522_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='casilla',
            name='borde',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='casilla',
            name='x',
            field=models.CharField(max_length=2),
        ),
        migrations.AlterField(
            model_name='casilla',
            name='y',
            field=models.CharField(max_length=2),
        ),
    ]