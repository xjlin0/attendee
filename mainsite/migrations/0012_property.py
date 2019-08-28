# Generated by Django 2.2 on 2019-08-27 03:34

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0011_campus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Address')),
                ('campus', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Campus')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_properties',
            },
        ),
    ]
