from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.TextField()

#permite que se muestre el texto en el admin
    def __str__(self):
        return self.text[:50]
