from django.db import models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length = required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=10000)
    summary     = models.TextField(blank=False, null=False)
    featured    = models.BooleanField(default=False) # null=True, default=True
    
#dynamically linking of URLS
    def  get_absolute_url(self): #a convention to grab the URL inside of django, so it's used in other places as well
        return f"/products/{self.id}/"
