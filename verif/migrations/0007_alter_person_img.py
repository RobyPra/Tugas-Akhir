# Generated by Django 3.2.6 on 2021-12-21 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verif', '0006_alter_person_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='img',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
