# Generated by Django 3.2.8 on 2022-03-22 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("effect_ae", "0002_auto_20220309_1441"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aeinitial",
            name="fluconazole_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                ],
                max_length=25,
                verbose_name="Relationship to study drugs: Fluconazole:",
            ),
        ),
        migrations.AlterField(
            model_name="historicalaeinitial",
            name="fluconazole_relation",
            field=models.CharField(
                choices=[
                    ("not_related", "Not related"),
                    ("unlikely_related", "Unlikely related"),
                    ("possibly_related", "Possibly related"),
                    ("probably_related", "Probably related"),
                    ("definitely_related", "Definitely related"),
                ],
                max_length=25,
                verbose_name="Relationship to study drugs: Fluconazole:",
            ),
        ),
    ]
