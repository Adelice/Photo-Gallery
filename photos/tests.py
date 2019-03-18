from django.test import TestCase
from .models import Image,Category,Location
# Create your tests here.
class ImageTest(TestCase):

    # def class instance setup for the project
    def setUp(self):
        self.rwanda = Location.objects.create(country='Rwanda')
       
        self.fun = Category.objects.create(name='fun')
        self.music = Category.objects.create(name='music')

        self.drinks = Image.objects.create(
            name='drinks', location=self.rwanda,  description='picture of a drinks')

        # self.drinks.Category.add(self.fun)
        # self.drinks.Category.add(self.music)

    
    def test_instance(self):
        self.drinks.save()
        self.assertTrue(isinstance(self.drinks, Image))

class CategoryTest(TestCase):
    def setUp(self):
        self.nature = Category(name='nature')

    def test_instance(self):
        self.nature.save()
        self.assertTrue(isinstance(self.nature, Category))
class LocationTest(TestCase):
    def setUp(self):
        self.rwanda = Location(country='rwanda')

    def test_instance(self):
        self.rwanda.save()
        self.assertTrue(isinstance(self.rwanda, Location))        