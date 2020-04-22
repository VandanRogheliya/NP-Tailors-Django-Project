from django.db import models

# class ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)


class BlouseImages(models.Model):
    img = models.ImageField(upload_to='BPics')


class ChaniyaCholiImages(models.Model):
    img = models.ImageField(upload_to='CCPics')


class DressesImages(models.Model):
    img = models.ImageField(upload_to='dressPics')


class HandWorkImages(models.Model):
    img = models.ImageField(upload_to='HWPics')
