from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin
 
class Campeon(models.Model):
    Nombre = models.CharField(max_length = 30)
    Titulo = models.CharField(max_length = 50)
    Icono = models.URLField(max_length = 200)
    Splashart = models.URLField(max_length = 200)
    Spotlight = models.URLField(max_length = 200)
    Habilidades = models.URLField(max_length = 200)
    Historia = models.URLField(max_length = 200)
    def __unicode__(self):
        return self.Nombre
    class Meta:
        verbose_name_plural = 'Campeon'

class PosesionCampeon(models.Model):
    Usuario = models.ForeignKey(User)
    Campeon = models.ForeignKey(Campeon)
    Posesion = models.BooleanField(default=False)
        class Meta:
        verbose_name_plural = 'PosesionCampeon'

admin.site.register(Campeon)
admin.site.register(PosesionCampeon)