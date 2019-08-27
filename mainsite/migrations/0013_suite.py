# Generated by Django 2.2 on 2019-08-27 03:37

from django.db import migrations, models

from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0012_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Property')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('location', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
        ),
    ]
