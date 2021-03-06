# Generated by Django 3.2.6 on 2022-01-29 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0014_auto_20220113_1555'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastFace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_face', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.BigIntegerField(blank=True, max_length=20, null=True),
        ),
    ]
