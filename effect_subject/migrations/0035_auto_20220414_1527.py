# Generated by Django 3.2.8 on 2022-04-14 13:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effect_subject', '0034_auto_20220414_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='fluconazole_dose_other',
            field=models.IntegerField(blank=True, help_text='in mg/d', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1199)], verbose_name='Other Fluconazole dose (if taken < 1 week prior to randomisation):'),
        ),
        migrations.AlterField(
            model_name='historicalpatienttreatmentday14',
            name='fluconazole_rx_d14_other',
            field=models.IntegerField(blank=True, help_text='in mg/d', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1199)], verbose_name='Other Fluconazole dose prescribed:'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='fluconazole_dose_other',
            field=models.IntegerField(blank=True, help_text='in mg/d', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1199)], verbose_name='Other Fluconazole dose (if taken < 1 week prior to randomisation):'),
        ),
        migrations.AlterField(
            model_name='patienttreatmentday14',
            name='fluconazole_rx_d14_other',
            field=models.IntegerField(blank=True, help_text='in mg/d', null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(1199)], verbose_name='Other Fluconazole dose prescribed:'),
        ),
    ]
