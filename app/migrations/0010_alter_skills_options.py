# Generated by Django 4.1.6 on 2023-02-06 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_skills_jobpost_skills'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='skills',
            options={'verbose_name': 'Skill', 'verbose_name_plural': 'Skills'},
        ),
    ]