# Generated by Django 5.1.3 on 2024-11-09 19:36

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Emotion",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("emotion", models.CharField(max_length=50)),
                (
                    "intensity",
                    models.IntegerField(
                        choices=[
                            (1, 1),
                            (2, 2),
                            (3, 3),
                            (4, 4),
                            (5, 5),
                            (6, 6),
                            (7, 7),
                            (8, 8),
                            (9, 9),
                            (10, 10),
                        ],
                        default=5,
                    ),
                ),
                ("note", models.TextField(blank=True, null=True)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-timestamp"],
            },
        ),
    ]
