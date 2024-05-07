# Generated by Django 5.0.4 on 2024-04-17 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Admin', '0001_initial'),
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscription_amount', models.CharField(max_length=20)),
                ('subscription_details', models.CharField(max_length=500)),
                ('subscription_duration', models.CharField(max_length=100, null=True)),
                ('coach', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Guest.tbl_coach')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_trainig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('training_duration', models.CharField(max_length=20)),
                ('training_details', models.CharField(max_length=500)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Guest.tbl_coach')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_event')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_dailyplan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dailyplan_day', models.CharField(max_length=20)),
                ('dailyplan_wcount', models.CharField(max_length=20)),
                ('training', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coach.tbl_trainig')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_workout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(max_length=20)),
                ('workout_discription', models.CharField(max_length=500)),
                ('workout_file', models.FileField(upload_to='workout-file/')),
                ('dailyplan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Coach.tbl_dailyplan')),
            ],
        ),
    ]
