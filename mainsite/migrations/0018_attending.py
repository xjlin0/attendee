# Generated by Django 2.2 on 2019-05-19 13:01

from django.db import migrations, models
from django.core.validators import MinValueValidator
from mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0017_relationship_m2m'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attending',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendee', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Attendee')),
                ('registration', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Registration')),
                ('price', models.DecimalField(decimal_places=2, default=999999, max_digits=8, validators=[MinValueValidator(0)])),
                ('age', models.IntegerField(blank=True, null=True)),
                ('attending_type', models.CharField(max_length=20, null=True)),
                ('belief', models.CharField(max_length=20, null=True)),
                ('bed_needs', models.IntegerField(default=1)),
                ('mobility', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'db_table': 'mainsite_attendings',
                'ordering': ['registration'],
            },
        ),
    ]
