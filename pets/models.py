from django.db import models


class Pet(models.Mode):
    id = models.AutoField(primary_key=True)
    breed = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_kids_friendly = models.BooleanField(default=False)
    description = models.TextField()
    image = models.ImageField(upload_to='pet_images/')

    def __str__(self):
        return '{0} ({1}) - id: {3}'.format(self.breed, self.name.upper(), str(self.id))
    

