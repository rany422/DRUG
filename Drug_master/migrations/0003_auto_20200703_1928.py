# Generated by Django 2.2.12 on 2020-07-03 13:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Drug_master', '0002_auto_20200703_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generic_information',
            name='drug_master',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drug', to='Drug_master.Drug_Master'),
        ),
    ]