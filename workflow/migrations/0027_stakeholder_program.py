# Generated by Django 2.2 on 2019-09-08 03:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0026_auto_20190907_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='program',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workflow.Program'),
        ),
    ]
