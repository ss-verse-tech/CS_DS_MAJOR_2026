from django.db import models

# Create your models here.
class To_Do_List(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=30)
    done = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    
