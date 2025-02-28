# Generated by Django 4.1.3 on 2023-05-17 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stroycontrol", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=20)),
                ("last_name", models.CharField(max_length=20)),
                ("password", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("age", models.IntegerField()),
            ],
        ),
    ]
