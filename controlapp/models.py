from django.db import models

class Switches(models.Model):
    username = models.CharField(max_length=20)
    switch_1 = models.BooleanField(default=False)
    switch_2 = models.BooleanField(default=False)
    switch_3 = models.BooleanField(default=False)
    switch_4 = models.BooleanField(default=False)
    switch_5 = models.BooleanField(default=False)

