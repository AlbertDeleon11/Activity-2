# Generated by Django 5.1.1 on 2025-01-02 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='is_student',
        ),
    ]