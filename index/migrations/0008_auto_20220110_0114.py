# Generated by Django 3.2 on 2022-01-09 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_auto_20220109_1426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_subj',
            field=models.CharField(choices=[('Maths', 'Maths'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry')], max_length=20),
        ),
        migrations.AlterField(
            model_name='notes',
            name='subject',
            field=models.CharField(choices=[('Maths', 'Maths'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry')], max_length=50),
        ),
    ]
