# Generated by Django 4.1.1 on 2022-09-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='send_email',
            field=models.BooleanField(default=True),
        ),
    ]
