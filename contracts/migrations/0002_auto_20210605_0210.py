# Generated by Django 3.2.4 on 2021-06-04 22:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contracts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='individual_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.individualperson'),
        ),
        migrations.AlterField(
            model_name='person',
            name='juridical_person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contracts.juridicalperson'),
        ),
    ]
