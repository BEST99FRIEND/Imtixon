from django.db import models

class Countries(models.Model):
    name = models.CharField(max_length=100, unique=True)
    place = models.CharField(max_length=100, default='')
    population = models.DecimalField(max_digits=15, decimal_places=2)
    territory = models.DecimalField(max_digits=15, decimal_places=2)
    ticket_price = models.PositiveBigIntegerField()
    image = models.FileField(upload_to='countries_images/')

    def __str__(self):
        return self.name