from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=200)
    no_of_guests= models.IntegerField(default=0)
    booking_date = models.DateField()

    def __str__(self): 
        return self.name

# Add code to create Menu model
class Menu(models.Model):
    title = models.CharField(max_length=200) 
    price = models.IntegerField(null=False) 
    inventory = models.IntegerField(default=0)
    #menu_item_description = models.TextField(max_length=1000, default='') 

    def __str__(self):
        return self.title
