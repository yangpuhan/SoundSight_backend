# Generated by Django 4.1.3 on 2023-12-21 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gpt_related', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioinfo',
            name='created_time',
            field=models.FloatField(default=1703167558.567317),
        ),
        migrations.AlterField(
            model_name='fullaudio',
            name='updated_time',
            field=models.FloatField(default=1703167558.567317),
        ),
    ]
