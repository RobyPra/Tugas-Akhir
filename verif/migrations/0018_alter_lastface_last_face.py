# Generated by Django 3.2.6 on 2022-01-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0017_lastface_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastface',
            name='last_face',
            field=models.CharField(default='Unknown', max_length=200),
        ),
    ]
