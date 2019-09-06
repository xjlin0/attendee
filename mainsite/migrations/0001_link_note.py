# Generated by Django 2.2 on 2019-05-19 13:00

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0000_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_table', models.CharField(db_index=True, max_length=50)),
                ('link_id', models.IntegerField(db_index=True)),
                ('note_type', models.CharField(blank=True, max_length=20, null=True)),
                ('note_text', models.CharField(max_length=2000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_link_notes',
                'ordering': ('-updated_at',),
            },
        ),
    ]
