# Generated by Django 5.0.7 on 2024-08-03 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=35)),
                ('Last_name', models.CharField(max_length=35)),
                ('father_name', models.CharField(max_length=35)),
                ('roll_number', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
                ('passing_year', models.CharField(max_length=30)),
            ],
        ),
    ]
