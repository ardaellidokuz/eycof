# Generated by Django 3.2 on 2021-04-24 23:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('builds', '0008_comments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buildorders',
            name='age',
            field=models.CharField(max_length=40, verbose_name='Çağ'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='buildorder',
            field=models.TextField(verbose_name='Build Order'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='explanation',
            field=models.CharField(max_length=100, verbose_name='Açıklama'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='headline',
            field=models.CharField(max_length=40, verbose_name='Başlık'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Yayınlanma Tarihi'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Kullanıcı Adı'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='vote',
            field=models.IntegerField(verbose_name='Oy'),
        ),
        migrations.AlterField(
            model_name='buildorders',
            name='writer',
            field=models.CharField(max_length=30, verbose_name='Yazar'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='combuild',
            field=models.CharField(max_length=400, verbose_name="Build Order'ın adı"),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comtext',
            field=models.TextField(verbose_name='Yorum'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comuser',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Yorumu Yapan Kullanıcı'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='pub_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Yayınlanma Tarihi'),
        ),
    ]
