# Generated by Django 3.1 on 2020-09-04 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('winupdate', '0003_auto_20200828_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='winupdatepolicy',
            name='critical',
            field=models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('inherit', 'Inherit')], default='manual', max_length=100),
        ),
        migrations.AlterField(
            model_name='winupdatepolicy',
            name='important',
            field=models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('inherit', 'Inherit')], default='manual', max_length=100),
        ),
        migrations.AlterField(
            model_name='winupdatepolicy',
            name='low',
            field=models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('inherit', 'Inherit')], default='manual', max_length=100),
        ),
        migrations.AlterField(
            model_name='winupdatepolicy',
            name='moderate',
            field=models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('inherit', 'Inherit')], default='manual', max_length=100),
        ),
        migrations.AlterField(
            model_name='winupdatepolicy',
            name='other',
            field=models.CharField(choices=[('manual', 'Manual'), ('approve', 'Approve'), ('ignore', 'Ignore'), ('inherit', 'Inherit')], default='manual', max_length=100),
        ),
    ]