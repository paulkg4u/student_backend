from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length = 256)
    gender = models.CharField(max_length = 100)
    age = models.IntegerField(default = 1)
    siblings = models.CharField(max_length = 512)
    current_class = models.IntegerField(default = 1)
    gpa = models.FloatField(default=3)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    