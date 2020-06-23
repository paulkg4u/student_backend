from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 256)
    gender = models.CharField(max_length = 100)
    age = models.IntegerField(default = 1)
    siblings = models.CharField(max_length = 512)
    current_class = models.IntegerField(default = 1)
    gpa = models.FloatField(default=3)


    def __str__(self):
        return self.name

    