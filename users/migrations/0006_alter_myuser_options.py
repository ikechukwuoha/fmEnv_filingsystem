# Generated by Django 4.2 on 2023-05-01 12:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_rename_staffprofile_profile_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="myuser",
            options={
                "permissions": (
                    ("GIS_STAFF", "All Permissions"),
                    ("STAFF", "Can add Names"),
                )
            },
        ),
    ]
