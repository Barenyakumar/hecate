# Generated by Django 3.2.3 on 2021-11-14 04:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literacy', models.CharField(max_length=200)),
                ('age', models.CharField(max_length=200)),
                ('sex', models.CharField(max_length=10)),
                ('full_name', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('patient_email_id', models.CharField(max_length=200)),
                ('doctor_name', models.CharField(max_length=200)),
                ('medical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.medical')),
            ],
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('frequency', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=200)),
                ('food', models.CharField(max_length=200)),
                ('prescription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eprescribe.prescription')),
            ],
        ),
    ]