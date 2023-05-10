# Generated by Django 4.2 on 2023-05-09 12:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_alter_myuser_sign_up_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="sign_up_date",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
