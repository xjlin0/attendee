# Generated by Django 2.2 on 2019-08-27 13:55

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0015_room'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProgramSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_group', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.ProgramGroup')),
                ('program_progression', models.ForeignKey(on_delete=models.SET(0), to='mainsite.ProgramProgression')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('start_at', models.DateTimeField(auto_now_add=True)),
                ('end_at', models.DateTimeField(auto_now_add=True, blank=True, null=True)),
                ('site_type', models.ForeignKey(on_delete=models.SET(0), to='contenttypes.ContentType', help_text='location: django_content_type id for table name')),
                ('site_id', models.BigIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_program_sessions',
            },
        ),
        migrations.AddConstraint(
            model_name='programsession',
            constraint=models.UniqueConstraint(fields=('program_group_id', 'site_type_id', 'site_id', 'start_at'), name='uniq_group_location_time'),
        ),
        migrations.AddField(
            model_name='programgroup',
            name='program_progressions',
            field=models.ManyToManyField(through='mainsite.ProgramSession', to='mainsite.ProgramProgression'),
        ),
        migrations.AddField(
            model_name='programprogression',
            name='program_progressions',
            field=models.ManyToManyField(through='mainsite.ProgramSession', to='mainsite.ProgramGroup'),
        ),
    ]
