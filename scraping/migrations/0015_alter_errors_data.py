# Generated by Django 4.1.1 on 2022-09-19 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraping', '0014_alter_errors_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errors',
            name='data',
            field=models.JSONField(default=dict),
        ),
    ]
