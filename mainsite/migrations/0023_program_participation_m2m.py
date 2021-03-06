# Generated by Django 2.2.5 on 2019-09-20 14:02

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0022_program_team'),
    ]
    operations = [
        migrations.CreateModel(
            name='ProgramParticipation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attending', models.ForeignKey(on_delete=models.SET(0), to='mainsite.Attending')),
                ('character', models.ForeignKey(on_delete=models.SET(0), to='mainsite.Character')),
                ('program_session', models.ForeignKey(on_delete=models.SET(0), to='mainsite.ProgramSession')),
                ('program_team', models.ForeignKey(blank=True, default=None, help_text='empty for main group', null=True, on_delete=models.deletion.SET_NULL, to='mainsite.ProgramTeam')),
                ('free', models.IntegerField(blank=True, default=0, help_text='multitasking: the person cannot join other sessions if negative', null=True)),
                ('attend_at', models.DateTimeField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_program_participations',
            },
        ),
        migrations.AddField(
            model_name='attending',
            name='program_sessions',
            field=models.ManyToManyField(through='mainsite.ProgramParticipation', to='mainsite.ProgramSession'),
        ),
        migrations.AddField(
            model_name='programsession',
            name='attendings',
            field=models.ManyToManyField(through='mainsite.ProgramParticipation', to='mainsite.Attending'),
        ),
    ]

