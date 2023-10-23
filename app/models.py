from django.db import models


# Create your models here.
# name of class indicates, table name in database
# Note : It is important to define max_length as a parameter whenever you are using CharFiled.
class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    roll_number = models.IntegerField()
    section = models.CharField(max_length=3)

    def __str__(self):
        return self.name
