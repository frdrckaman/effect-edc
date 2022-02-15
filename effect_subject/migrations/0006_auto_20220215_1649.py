# Generated by Django 3.2.8 on 2022-02-15 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('effect_lists', '0003_auto_20220215_1625'),
        ('effect_subject', '0005_auto_20220215_1625'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsignsandsymptoms',
            name='any_sx',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('unknown', 'Unknown')], max_length=15, verbose_name='Are there any signs or symptoms to report, since last contact with trial team?'),
        ),
        migrations.AlterField(
            model_name='signsandsymptoms',
            name='any_sx',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('unknown', 'Unknown')], max_length=15, verbose_name='Are there any signs or symptoms to report, since last contact with trial team?'),
        ),
        migrations.AlterField(
            model_name='signsandsymptoms',
            name='current_sx',
            field=models.ManyToManyField(related_name='sx', to='effect_lists.SiSx', verbose_name='Is patient currently experiencing any of the following signs/symptoms?'),
        ),
    ]
