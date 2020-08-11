# Generated by Django 3.0.5 on 2020-08-11 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0014_remove_person_current_role_division_id"),
    ]

    operations = [
        migrations.RemoveField(model_name="billaction", name="extras",),
        migrations.RemoveField(model_name="billdocument", name="extras",),
        migrations.AlterIndexTogether(
            name="membership", index_together={("organization", "person", "post")},
        ),
        migrations.RemoveField(model_name="membership", name="label",),
    ]