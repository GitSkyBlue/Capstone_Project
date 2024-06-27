from django.db import models

# Create your models here.

class JsonData(models.Model):
    data = models.JSONField(unique=True)

    def __str__(self):
        return str(self.data["name"]+" - "+self.data["time"])