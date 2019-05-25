# Generated by Django 2.2 on 2019-05-19 13:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
from  mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_label', models.CharField(default='2019 summer retreat', max_length=50)),
                ('price_type', models.CharField(db_index=True, max_length=20)),
                ('start_date', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('price_value', models.DecimalField(decimal_places=2, default=999999, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
                ('event', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainsite.Event')),
            ],
        ),
    ]