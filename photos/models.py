from django.db import models

# Create your models here.
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.CharField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    # image_location = models.ForeignKey(Location)
    # image_category = models.ForeignKey(Category)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()    
    class Meta:
        ordering = ['name']    
class Location(models.Model):
    country = models.CharField(max_length =30)
    city = models.CharField(max_length =30)
    def __str__(self):
        return self.country
class Category(models.Model):
    category = models.CharField(max_length =30) 
    def __str__(self):
        return self.category         