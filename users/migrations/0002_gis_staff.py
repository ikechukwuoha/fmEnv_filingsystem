# Generated by Django 4.2 on 2023-04-27 00:14

from django.db import migrations
import django.db.models.manager
import users.managers


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gis_staff",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("users.myuser",),
            managers=[
                ("gis_staff", django.db.models.manager.Manager()),
                ("objects", users.managers.MyUserManager()),
            ],
        ),
    ]