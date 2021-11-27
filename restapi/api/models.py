from django.db import models

# Create your models here.
class Booking(models.Model):
    time_slot = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.timestamp)