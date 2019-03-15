from django.db import models
import datetime as dt
# Create your models here.
class Location(models.Model):
    country = models.CharField(max_length =30)
    city = models.CharField(max_length =30)
    def __str__(self):
        return self.country
class Category(models.Model):
    category = models.CharField(max_length =30) 
    def __str__(self):
        return self.category         
class Image(models.Model):
    image=models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length =30)
    description = models.TextField(max_length =30)
    pub_date = models.DateTimeField(auto_now_add=True)
    image_location = models.ForeignKey(Location, null=True)
    image_category = models.ForeignKey(Category, null=True)
    def __str__(self):
        return self.name
    def save_image(self):
        self.save()  
    @classmethod
    def get_image(cls,id):
        try:
            image=Image.objects.get(id=id)
            return image
        except DoesNotExist:
            return Image.objects.get(id=1) 
    @classmethod
    def search_by_category(cls,search_images):
        images = Image.objects.filter(categories__name__icontains=search_images)
        return images         
    class Meta:
        ordering = ['name']    
