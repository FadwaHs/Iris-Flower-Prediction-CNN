# Generated by Django 2.2.20 on 2021-06-11 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='predresults',
            name='score',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
