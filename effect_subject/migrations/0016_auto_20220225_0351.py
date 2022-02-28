# Generated by Django 3.2.11 on 2022-02-25 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('effect_subject', '0015_auto_20220224_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodculture',
            name='requisition',
            field=models.ForeignKey(blank=True, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='effect_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='histopathology',
            name='requisition',
            field=models.ForeignKey(blank=True, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='effect_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='historicalbloodculture',
            name='requisition',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='effect_subject.subjectrequisition', verbose_name='Requisition'),
        ),
        migrations.AddField(
            model_name='historicalhistopathology',
            name='requisition',
            field=models.ForeignKey(blank=True, db_constraint=False, help_text='Start typing the requisition identifier or select one from this visit', null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='effect_subject.subjectrequisition', verbose_name='Requisition'),
        ),
    ]
