# Generated by Django 4.1.3 on 2023-11-25 15:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_alter_user_created_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_time',
            field=models.FloatField(default=1700925245.725665),
        ),
        migrations.AlterField(
            model_name='userhistory',
            name='created_time',
            field=models.FloatField(default=1700925245.724774),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created_time',
            field=models.FloatField(default=1700925245.725665),
        ),
        migrations.CreateModel(
            name='AudioInfo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('checkCode', models.CharField(max_length=64)),
                ('instruction', models.CharField(max_length=64)),
                ('text', models.TextField()),
                ('created_time', models.FloatField(default=1700925245.726671)),
                ('updated_time', models.FloatField(default=1700925245.726671)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddIndex(
            model_name='audioinfo',
            index=models.Index(fields=['checkCode'], name='user_auth_a_checkCo_284226_idx'),
        ),
    ]