# Generated by Django 2.2 on 2019-05-19 13:01

from django.db import migrations, models

from  mainsite.models.enum import RecordStatusEnum


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0005_price'),
    ]
    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apply_type', models.CharField(max_length=20, null=True)),
                ('apply_key', models.CharField(max_length=50, null=True)),
                ('event', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Event')),
                ('main_attendee', models.ForeignKey(null=True, on_delete=models.deletion.SET_NULL, to='mainsite.Attendee')),
                ('donation', models.DecimalField(decimal_places=2, default=999999, max_digits=8)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=RecordStatusEnum.choices(), db_index=True, default=RecordStatusEnum.ACTIVE, max_length=10)),
            ],
            options={
                'ordering': ['main_attendee__english_name', 'main_attendee__chinese_name'],
            },
        ),
    ]

