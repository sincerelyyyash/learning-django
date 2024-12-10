# Generated by Django 5.1.3 on 2024-12-09 11:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ChaiVariety",
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
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="chais/")),
                ("date_added", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("ML", "MASALA"),
                            ("GR", "GINGER"),
                            ("PL", "PLAIN"),
                            ("LM", "LEMON"),
                        ],
                        max_length=2,
                    ),
                ),
            ],
        ),
    ]
