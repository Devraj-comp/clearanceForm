import datetime

from django.db import models
from django.contrib.auth.models import User

# Create your models here.


CLEARANCE_CHOICES= [
    ('all clear', 'All Clear'),
    ('semi clear', 'Semi Clear')
    ]

class clearanceModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    department = models.CharField(max_length = 200)
    cleared_by = models.CharField(max_length=200)
    date = models.DateField(("Date"), default=datetime.date.today)
    clearance = models.CharField(max_length=200, choices=CLEARANCE_CHOICES, default='All Clear')
    sign = models.CharField(max_length = 200)

    def __str__(self):
        return self.department