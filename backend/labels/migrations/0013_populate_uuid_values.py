# Generated by Django 4.0.2 on 2022-05-12 02:28

import uuid

from django.db import migrations


def gen_uuid(apps, schema_editor):
    Category = apps.get_model("labels", "Category")
    Span = apps.get_model("labels", "Span")
    Relation = apps.get_model("labels", "Relation")
    TextLabel = apps.get_model("labels", "TextLabel")
    for label in [Category, Span, Relation, TextLabel]:
        for row in label.objects.all():
            row.uuid = uuid.uuid4()
            row.save(update_fields=["uuid"])


class Migration(migrations.Migration):

    dependencies = [
        ("labels", "0012_add_uuid_field"),
    ]

    operations = [
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
