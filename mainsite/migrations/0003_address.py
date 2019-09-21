# Generated by Django 2.2 on 2019-05-19 13:00

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_attendee'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email1', models.EmailField(blank=True, db_index=True, null=True, max_length=190)),
                ('email2', models.EmailField(blank=True, null=True, max_length=190)),
                ('phone1', models.CharField(blank=True, db_index=True, max_length=15, null=True)),
                ('phone2', models.CharField(blank=True, max_length=15, null=True)),
                ('address_type', models.CharField(max_length=20, null=True)),
                ('street1', models.CharField(blank=True, max_length=50, null=True)),
                ('street2', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(default='CA', max_length=10)),
                ('zip_code', models.CharField(max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_addresses',
            },
        ),
    ]
