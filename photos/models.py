from django.db import models

# Create your models here.
class Image(models.Model):
    Image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    # image_location = models.ForeignKey(Location)
    # image_category = models.ForeignKey(Category)