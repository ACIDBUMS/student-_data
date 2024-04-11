from django.db import models

# Create your models here.
class chai (models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    image=models.ImageField(upload_to='photo')
     
    def __str__(self):
        return self.name
    

class Form (models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    image=models.ImageField(upload_to='photo')

    
def __str__(self):
        return self.name
     
