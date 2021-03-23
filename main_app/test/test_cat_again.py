from django.test import TestCase

# Create your tests here.
from main_app.models import Cat

class CatTestCase(TestCase):
    def setUp(self):
        Cat.objects.create(name="Garfield", breed="Tabby", description="", age=9)
        Cat.objects.create(name="Oliver", breed="Tabby", description="Oliver and Company", age=5)

    def test_cat_names(self):
        """Cat that are identified by name"""
        garfield = Cat.objects.get(name="Garfield")
        oliver = Cat.objects.get(age=5)
        
        self.assertEqual(garfield.name, 'Garfield')
        self.assertEqual(oliver.name, 'Oliver')