from django.db import models
class Job(models.Model):
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    image1=models.ImageField(upload_to='images/',default=0)
    image2=models.ImageField(upload_to='images/',default=0)
    image3=models.ImageField(upload_to='images/',default=0)


