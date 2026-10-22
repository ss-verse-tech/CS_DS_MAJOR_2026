from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    department = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
