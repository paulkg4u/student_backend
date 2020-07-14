from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4

# Create your models here.
class Student(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gender = models.CharField(max_length = 100)
    age = models.IntegerField(default = 1)
    siblings = models.CharField(max_length = 512)
    current_class = models.IntegerField(default = 1)
    gpa = models.FloatField(default=3)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.first_name

    