# Generated by Django 2.2.12 on 2020-07-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drug_master', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generic_information',
            name='drug_master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Drug_master.Drug_Master'),
        ),
    ]
