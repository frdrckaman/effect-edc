# Generated by Django 3.2.8 on 2022-05-16 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('effect_ae', '0005_auto_20220504_0602'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aeinitial',
            old_name='fluconazole_relation',
            new_name='flucon_relation',
        ),
        migrations.RenameField(
            model_name='aeinitial',
            old_name='flucytosine_relation',
            new_name='flucyt_relation',
        ),
        migrations.RenameField(
            model_name='historicalaeinitial',
            old_name='fluconazole_relation',
            new_name='flucon_relation',
        ),
        migrations.RenameField(
            model_name='historicalaeinitial',
            old_name='flucytosine_relation',
            new_name='flucyt_relation',
        ),
    ]
