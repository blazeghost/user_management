# Generated by Django 3.2.4 on 2021-06-29 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210629_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table_one',
            name='date_time',
            field=models.DateTimeField(blank=True),
        ),
    ]