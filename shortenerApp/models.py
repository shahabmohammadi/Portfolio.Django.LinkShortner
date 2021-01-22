from django.db import models


# Create your models here.
class Urls(models.Model):
    url = models.URLField()
    click_count = models.PositiveBigIntegerField(default=0)
