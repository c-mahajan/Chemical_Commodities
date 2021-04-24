# Generated by Django 3.2 on 2021-04-21 04:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChemCompo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Chemical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('inventory', models.FloatField()),
                ('price', models.FloatField()),
                ('chem_compo', models.ManyToManyField(related_name='commodities', to='api.ChemCompo')),
            ],
        ),
        migrations.AddField(
            model_name='chemcompo',
            name='chemical',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compositions', to='api.chemical'),
        ),
    ]
