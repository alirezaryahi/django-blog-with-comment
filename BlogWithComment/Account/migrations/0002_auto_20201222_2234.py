# Generated by Django 3.1.4 on 2020-12-22 19:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='custom_user',
            options={},
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='phone',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='custom_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
