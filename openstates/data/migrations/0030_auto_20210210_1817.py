# Generated by Django 3.0.5 on 2021-02-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0029_auto_20210203_1946"),
    ]

    operations = [
        migrations.AlterField(
            model_name="relatedbill",
            name="relation_type",
            field=models.CharField(
                choices=[
                    ("companion", "Companion"),
                    ("prior-session", "Prior Session"),
                    ("replaced-by", "Replaced By"),
                    ("replaces", "Replaces"),
                    ("related", "Related"),
                ],
                max_length=100,
            ),
        ),
    ]