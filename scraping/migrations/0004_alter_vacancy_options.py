# Generated by Django 4.1.1 on 2022-09-16 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0003_url'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacancy',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Vacancy', 'verbose_name_plural': 'Vacancies'},
        ),
    ]