from django.db import models

from users.models import AppUser


class Offer(models.Model):
    type_used_vehicle = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    mileage = models.PositiveIntegerField(help_text="Mileage in km")
    fuel = models.CharField(max_length=50, choices=[
        ('Diesel', 'Diesel'),
        ('Petrol', 'Petrol'),
        ('Electric', 'Electric'),
        ('Hybrid', 'Hybrid'),
        ('Other', 'Other'),
    ])
    power = models.PositiveIntegerField(help_text="Power in hp")
    gearbox = models.CharField(max_length=50, choices=[
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        ('Other', 'Other'),
    ])
    number_of_seats = models.PositiveIntegerField()
    doors = models.CharField(max_length=10, choices=[
        ('2/3', '2/3'),
        ('4/5', '4/5'),
        ('Other', 'Other'),
    ])
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="offer_images/")
    short_description = models.CharField(max_length=500)
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="vehicles")
    price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField(blank=True, null=True)
    def __str__(self):
        return f"{self.title}"
