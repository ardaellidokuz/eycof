# Generated by Django 3.2 on 2021-04-22 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0002_alter_buildorders_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildorders',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
