import self
from django.test import TestCase
from .models import Student


class modelTest(TestCase):

    def test_model_exists(self):
        data = Student.objects.count()
        self.assertEquals(data, 0)

    def test_model_has_name(self):
        name = Student.objects.create(name="Hello")
        self.assertEquals(name, name.name)
