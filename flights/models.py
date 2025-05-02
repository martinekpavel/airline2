from django.db import models

# Create your models here.
class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
        return f"Město: {self.city} Kód: ({self.code})"
    
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")

    # https://www.youtube.com/watch?v=O5YkEFLXcRg

    def __str__(self):
        return f"id {self.id}: {self.origin} --> {self.destination} délka letu ({self.duration})"