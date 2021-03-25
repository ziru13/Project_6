from django.db import models


# Create your models here.
class Rock(models.Model):
    name = models.CharField(max_length=255)
    # category = models.CharField(max_length=255)
    # color = models.CharField(max_length=255)

    def __str__(self):
        return self.name
