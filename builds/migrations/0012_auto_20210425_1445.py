# Generated by Django 3.2 on 2021-04-25 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builds', '0011_buildorders_build_list'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='combuild',
        ),
        migrations.AddField(
            model_name='comments',
            name='combuildtitle',
            field=models.CharField(default=1, max_length=100, verbose_name='Yorum yapılan buildorder'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='comid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='builds.buildorders', verbose_name="Build Order'ın No"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='approved',
            field=models.BooleanField(default='False', verbose_name='Onay'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='build_list',
            field=models.CharField(default='', max_length=1000, verbose_name='Liste şeklinde'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='buildorder',
            field=models.TextField(blank=bool, default=' ', verbose_name='Build Order'),
        ),
    ]
