# Generated by Django 2.2.5 on 2019-09-21 15:18

from django.db import migrations, models
from recurrence.fields import RecurrenceField
from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('mainsite', '0023_program_participation_m2m'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramGroupSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_group', models.ForeignKey(on_delete=models.SET(0), to='mainsite.ProgramGroup')),
                ('site_type', models.ForeignKey(help_text='location: django_content_type id for table name', on_delete=models.SET(0), to='contenttypes.ContentType')),
                ('site_id', models.BigIntegerField()),
                ('recurrences', RecurrenceField()),
                ('start_time', models.TimeField(default='10:00')),
                ('duration', models.DurationField(default='01:00:00')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_program_group_settings',
            },
        ),
    ]
