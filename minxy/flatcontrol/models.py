from django.db import models


class TempSensor(models.Model):

    time = models.DateTimeField(auto_now_add=True)
    temp = models.DecimalField(max_digits=4, decimal_places=2)

