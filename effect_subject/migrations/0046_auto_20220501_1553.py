# Generated by Django 3.2.11 on 2022-05-01 12:53

import uuid

import _socket
import django.contrib.sites.managers
import django.db.models.deletion
import django_audit_fields.fields.hostname_modification_field
import django_audit_fields.fields.userfield
import django_audit_fields.fields.uuid_auto_field
import django_audit_fields.models.audit_model_mixin
import django_revision.revision_field
import edc_model.validators.date
import edc_protocol.validators
import edc_utils.date
import edc_visit_tracking.managers
import simple_history.models
from django.conf import settings
from django.db import migrations, models

import effect_subject.models.subject_visit


class Migration(migrations.Migration):

    dependencies = [
        ("sites", "0002_alter_domain_unique"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("effect_subject", "0045_auto_20220501_1551"),
    ]

    operations = [
        migrations.AlterField(
            model_name="historicalmedicationadherence",
            name="pill_count",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Number of pills left in the bottle"
            ),
        ),
        migrations.AlterField(
            model_name="medicationadherence",
            name="pill_count",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="Number of pills left in the bottle"
            ),
        ),
    ]
