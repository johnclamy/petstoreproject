from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    id = models.AutoField(primary_key=True)
    breed = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_kids_friendly = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/')

    def __str__(self):
        return '{0} ({1})'.format(self.breed, self.name.upper())
    

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    comments = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Review for {0} by {1}'.format(self.pet.name, self.user.username)
