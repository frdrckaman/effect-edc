# Generated by Django 3.2.11 on 2022-03-29 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effect_screening', '0012_auto_20220329_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsubjectscreening',
            name='cm_in_csf_method',
            field=models.CharField(choices=[('india_ink', 'positive microscopy with India Ink'), ('culture', 'culture'), ('OTHER', 'Other, please specify'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If YES, by which method?'),
        ),
        migrations.AlterField(
            model_name='subjectscreening',
            name='cm_in_csf_method',
            field=models.CharField(choices=[('india_ink', 'positive microscopy with India Ink'), ('culture', 'culture'), ('OTHER', 'Other, please specify'), ('N/A', 'Not applicable')], default='N/A', max_length=25, verbose_name='If YES, by which method?'),
        ),
    ]
