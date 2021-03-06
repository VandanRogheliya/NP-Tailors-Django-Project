# Generated by Django 3.0.5 on 2020-04-14 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StaticSite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurements',
            name='NapeToWaist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='NeckToWaist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='aroundAnkle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='aroundCalf',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='aroundKnee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='aroundKnuckle',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='belowButtockToheel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='bicep',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='braSize',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='bust',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='footWidth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='frontWaistToBelowKnee',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='frontWaistToHeel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='head',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='height',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='highHip',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='hip',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='insideArm',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='insideLegToHeel',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='neck',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='neckToShoulder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='nippleToNipple',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='nippleToShoulder',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='rise',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='shoulderWidth',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='topOfThigh',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='underBust',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='underBustToWaist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='underarmToWaist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='upperBust',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waist',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='waistToCrotchLine',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='measurements',
            name='wrist',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
