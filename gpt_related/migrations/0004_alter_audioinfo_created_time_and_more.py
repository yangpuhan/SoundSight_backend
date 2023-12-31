# Generated by Django 4.1.3 on 2023-12-21 15:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gpt_related', '0003_alter_audioinfo_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audioinfo',
            name='created_time',
            field=models.FloatField(default=1703173296.098446),
        ),
        migrations.AlterField(
            model_name='fullaudio',
            name='updated_time',
            field=models.FloatField(default=1703173296.099455),
        ),
        migrations.CreateModel(
            name='AudioIntegration',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('integration', models.TextField(default='')),
                ('audio_id_list', models.TextField(default='')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
