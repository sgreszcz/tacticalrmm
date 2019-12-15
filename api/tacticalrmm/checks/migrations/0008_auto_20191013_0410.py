# Generated by Django 2.2.6 on 2019-10-13 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0007_auto_20190908_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='diskcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check')], default='diskspace', max_length=30),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='disk',
            field=models.CharField(blank=True, max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='more_info',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='status',
            field=models.CharField(choices=[('passing', 'Passing'), ('failing', 'Failing'), ('pending', 'Pending')], default='pending', max_length=30),
        ),
        migrations.AlterField(
            model_name='diskcheck',
            name='threshold',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='standardcheck',
            name='check_type',
            field=models.CharField(choices=[('diskspace', 'Disk Space Check'), ('ping', 'Ping Check'), ('cpuload', 'CPU Load Check'), ('memory', 'Memory Check')], max_length=30),
        ),
    ]