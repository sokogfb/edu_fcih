# Generated by Django 2.0.3 on 2018-03-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'male'), ('female', 'female')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='student_profile',
            name='religion',
            field=models.CharField(blank=True, choices=[('muslim', 'muslim'), ('christian', 'christian')], max_length=50, null=True),
        ),
    ]
