from django.db import models

# Create your models here.


class Measurements(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    braSize = models.FloatField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    head = models.FloatField(null=True, blank=True)
    neck = models.FloatField(null=True, blank=True)
    upperBust = models.FloatField(null=True, blank=True)
    bust = models.FloatField(null=True, blank=True)
    nippleToNipple = models.FloatField(null=True, blank=True)
    nippleToShoulder = models.FloatField(null=True, blank=True)
    underBust = models.FloatField(null=True, blank=True)
    waist = models.FloatField(null=True, blank=True)
    highHip = models.FloatField(null=True, blank=True)
    hip = models.FloatField(null=True, blank=True)
    shoulderWidth = models.FloatField(null=True, blank=True)
    bicep = models.FloatField(null=True, blank=True)
    wrist = models.FloatField(null=True, blank=True)
    insideArm = models.FloatField(null=True, blank=True)
    aroundKnuckle = models.FloatField(null=True, blank=True)
    topOfThigh = models.FloatField(null=True, blank=True)
    insideLegToHeel = models.FloatField(null=True, blank=True)
    aroundKnee = models.FloatField(null=True, blank=True)
    aroundCalf = models.FloatField(null=True, blank=True)
    aroundAnkle = models.FloatField(null=True, blank=True)
    footWidth = models.FloatField(null=True, blank=True)
    belowButtockToheel = models.FloatField(null=True, blank=True)
    frontWaistToHeel = models.FloatField(null=True, blank=True)
    frontWaistToBelowKnee = models.FloatField(null=True, blank=True)
    NeckToWaist = models.FloatField(null=True, blank=True)
    waistToCrotchLine = models.FloatField(null=True, blank=True)
    underBustToWaist = models.FloatField(null=True, blank=True)
    rise = models.FloatField(null=True, blank=True)
    NapeToWaist = models.FloatField(null=True, blank=True)
    neckToShoulder = models.FloatField(null=True, blank=True)
    underarmToWaist = models.FloatField(null=True, blank=True)

