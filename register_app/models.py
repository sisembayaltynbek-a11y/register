from django.db import models

# Create your models here.
class Register(models.Model):
    fullname = models.CharField(max_length=255)
    schoolname = models.CharField(max_length=255)
    area = models.CharField(max_length=255)

    def __str__(self):
        return self.fullname