# Generated by Django 4.2 on 2023-05-09 13:08

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0011_myuser_group"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="myuser",
            options={"verbose_name": "user", "verbose_name_plural": "users"},
        ),
        migrations.RemoveField(
            model_name="myuser",
            name="group",
        ),
    ]