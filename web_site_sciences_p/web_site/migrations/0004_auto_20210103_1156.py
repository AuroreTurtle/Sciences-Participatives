# Generated by Django 3.1.2 on 2021-01-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0003_auto_20210102_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='N_matricule',
            field=models.CharField(max_length=25, verbose_name='N° matricule'),
        ),
    ]