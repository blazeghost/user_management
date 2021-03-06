# Generated by Django 3.2.4 on 2021-06-28 14:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Master_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=50)),
                ('Password', models.CharField(max_length=50)),
                ('Role', models.CharField(max_length=50)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_updated', models.DateTimeField(auto_now_add=True)),
                ('is_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=50)),
                ('Lastname', models.CharField(max_length=50)),
                ('m_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.master_table')),
            ],
        ),
        migrations.CreateModel(
            name='Table_two',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=50)),
                ('visitor_purpose', models.CharField(max_length=50)),
                ('visitor_contact', models.CharField(max_length=50)),
                ('visitor_address', models.CharField(max_length=100)),
                ('visitor_vehicle_number', models.CharField(max_length=50)),
                ('concerned_person', models.CharField(max_length=50)),
                ('date_time', models.DateField(default='2020-12-01')),
                ('s_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Table_one',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visitor_name', models.CharField(max_length=50)),
                ('visitor_purpose', models.CharField(max_length=50)),
                ('visitor_contact', models.CharField(max_length=50)),
                ('concerned_person', models.CharField(max_length=50)),
                ('date_time', models.DateField(default='2020-12-01')),
                ('a_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
