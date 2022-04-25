# Generated by Django 3.2.8 on 2022-04-21 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effect_subject', '0039_auto_20220420_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpatienthistory',
            name='current_arv_decision',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('art_continued', 'ART continued'), ('art_stopped', 'ART stopped')], default='N/A', max_length=25, verbose_name='What decision was made at enrolment regarding their <u>current</u> ART regimen?'),
        ),
        migrations.AlterField(
            model_name='historicalsubjectvisit',
            name='hospitalized',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('unknown', 'Unknown')], default='N/A', help_text='If YES, complete AE Initial report.', max_length=15, verbose_name='Has the patient been hospitalized since the last assessment?'),
        ),
        migrations.AlterField(
            model_name='patienthistory',
            name='current_arv_decision',
            field=models.CharField(choices=[('N/A', 'Not applicable'), ('art_continued', 'ART continued'), ('art_stopped', 'ART stopped')], default='N/A', max_length=25, verbose_name='What decision was made at enrolment regarding their <u>current</u> ART regimen?'),
        ),
        migrations.AlterField(
            model_name='subjectvisit',
            name='hospitalized',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('unknown', 'Unknown')], default='N/A', help_text='If YES, complete AE Initial report.', max_length=15, verbose_name='Has the patient been hospitalized since the last assessment?'),
        ),
    ]
