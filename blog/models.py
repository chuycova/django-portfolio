from django.db import models
from django.db.models.fields import DateField
from datetime import date

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, default="D")
    date = models.DateField(blank=True, default=date.today)
    date2 = models.DateField(blank=True, auto_now_add=True)

    def __str__(self):
        return self.titulo
