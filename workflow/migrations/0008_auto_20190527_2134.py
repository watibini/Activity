# Generated by Django 2.2.1 on 2019-05-28 04:34

from django.db import migrations, models
import uuid


def gen_uuid(apps, schema_editor):
    program = apps.get_model('workflow', 'Program')
    for row in program.objects.all():
        row.program_uuid = uuid.uuid4()
        row.save(update_fields=['program_uuid'])


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0007_auto_20190527_2120'),
    ]

    operations = [
        # omit reverse_code=... if you don't want the migration to be reversible.
        migrations.RunPython(gen_uuid, reverse_code=migrations.RunPython.noop),
    ]
