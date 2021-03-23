from django.test import TestCase

# Create your tests here.
from main_app.models import Cat

class CatTestCase(TestCase):
    def setUp(self):
        Cat.objects.create(name="Roar", breed="Tiger", description="A tiger", age=11)
        Cat.objects.create(name="Rumble", breed="Tiger", description="A tiger", age=11)

    def test_cat_names(self):
        """Cat that are identified by name"""
        roar = Cat.objects.get(name="Roar")
        rumble = Cat.objects.get(name="Rumble")
        
        self.assertEqual(roar.name, 'Roar')
        self.assertEqual(rumble.name, 'Rumble')