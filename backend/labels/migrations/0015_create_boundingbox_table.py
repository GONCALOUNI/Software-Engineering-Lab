# Generated by Django 4.0.4 on 2022-06-29 06:19

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("label_types", "0007_delete_relationtypeold"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("examples", "0006_alter_example_upload_name"),
        ("labels", "0014_remove_uuid_null"),
    ]

    operations = [
        migrations.CreateModel(
            name="BoundingBox",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("uuid", models.UUIDField(default=uuid.uuid4, unique=True)),
                ("prob", models.FloatField(default=0.0)),
                ("manual", models.BooleanField(default=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("x", models.FloatField()),
                ("y", models.FloatField()),
                ("width", models.FloatField()),
                ("height", models.FloatField()),
                (
                    "example",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="bboxes", to="examples.example"
                    ),
                ),
                (
                    "label",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="label_types.categorytype"),
                ),
                ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name="boundingbox",
            constraint=models.CheckConstraint(check=models.Q(("x__gte", 0)), name="x >= 0"),
        ),
        migrations.AddConstraint(
            model_name="boundingbox",
            constraint=models.CheckConstraint(check=models.Q(("y__gte", 0)), name="y >= 0"),
        ),
        migrations.AddConstraint(
            model_name="boundingbox",
            constraint=models.CheckConstraint(check=models.Q(("width__gte", 0)), name="width >= 0"),
        ),
        migrations.AddConstraint(
            model_name="boundingbox",
            constraint=models.CheckConstraint(check=models.Q(("height__gte", 0)), name="height >= 0"),
        ),
    ]
