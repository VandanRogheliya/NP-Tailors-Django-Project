# Generated by Django 3.0.5 on 2020-04-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaticSite', '0002_auto_20200414_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurements',
            name='first_name',
            field=models.CharField(default='firstName', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='measurements',
            name='last_name',
            field=models.CharField(default='lastName', max_length=30),
            preserve_default=False,
        ),
    ]