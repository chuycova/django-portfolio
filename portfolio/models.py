from django.db import models

class Project(models.Model):
    titulo= models.CharField(max_length=100)
    descripcion= models.CharField(max_length=250, blank=True)
    imagen = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    #archivo1 = models.CharField(max_length=200)
    #archivo2 = models.CharField(max_length=200)

    def __str__(self):
        return self.titulo

