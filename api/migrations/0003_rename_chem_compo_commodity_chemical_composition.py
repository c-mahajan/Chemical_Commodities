# Generated by Django 3.2 on 2021-04-21 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_rename_chemical_chemcompo_element'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commodity',
            old_name='chem_compo',
            new_name='chemical_composition',
        ),
    ]
