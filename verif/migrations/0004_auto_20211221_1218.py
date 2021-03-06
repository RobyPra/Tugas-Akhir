# Generated by Django 3.2.6 on 2021-12-21 05:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0003_auto_20211209_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbface', models.CharField(max_length=120)),
                ('last_modified', models.DateTimeField(auto_now_add=True)),
                ('faceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verif.person')),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='verif.vehicle')),
            ],
        ),
        migrations.DeleteModel(
            name='Owner',
        ),
    ]
