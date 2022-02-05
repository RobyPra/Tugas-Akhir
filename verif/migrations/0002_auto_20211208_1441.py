# Generated by Django 3.2.6 on 2021-12-08 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log', models.CharField(choices=[('out', 'Out'), ('in', 'In')], max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('no_polisi', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('vehicleType', models.CharField(choices=[('motor', 'Motor'), ('mobil', 'Mobil')], max_length=10)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verif.visitor')),
            ],
        ),
        migrations.RemoveField(
            model_name='vehicles',
            name='owner',
        ),
        migrations.DeleteModel(
            name='Logs',
        ),
        migrations.DeleteModel(
            name='Vehicles',
        ),
        migrations.AddField(
            model_name='log',
            name='visitor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='verif.vehicle'),
        ),
    ]
