# Generated by Django 2.2 on 2019-08-25 22:29

from django.db import migrations, models
import mainsite.models.enum
from mainsite.models.enum import RecordStatusEnum
import mainsite.models.formatter


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0007_attending'),
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, db_index=True, max_length=50)),
                ('info', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=mainsite.models.enum.RecordStatusEnum('active'), max_length=10)),
            ],
            options={
                'db_table': 'mainsite_character',
            },
        ),
    ]
