# Generated by Django 4.1.7 on 2023-03-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0002_note_owner"),
    ]

    operations = [
        migrations.AddField(
            model_name="note",
            name="deleted",
            field=models.BooleanField(default=False),
        ),
    ]