from django.db import models

# Create your models here.
class Contact(models.Model):
    Name = models.CharField(max_length=100)
    Realtionship = models.CharField(max_length=50)
    Phone_no = models.CharField(max_length=12)
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.Name

