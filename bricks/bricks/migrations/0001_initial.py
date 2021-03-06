# Generated by Django 3.1.1 on 2020-10-01 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('building_id', models.AutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=1024)),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bricks_num', models.IntegerField()),
                ('date', models.DateField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bricks.building')),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
