from django.db import models

from users.models import AppUser


class AutoPart(models.Model):
    title = models.CharField(max_length=255)
    short_description = models.TextField()
    model = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    discounted_price = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='auto_parts_images/')
    owner = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name="auto_parts")

    def __str__(self):
        return self.title