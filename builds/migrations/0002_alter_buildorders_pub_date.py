# Generated by Django 3.2 on 2021-04-22 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildorders',
            name='pub_date',
            field=models.TimeField(auto_now=True),
        ),
    ]
