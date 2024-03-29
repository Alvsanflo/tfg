from django.db import models

class Jugador(models.Model):
    nombre = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    PIE_CHOICES = [
        ('Diestro', 'Diestro'),
        ('Zurdo', 'Zurdo'),
        ('Ambidiestro', 'Ambidiestro'),
    ]
    pie_bueno = models.CharField(max_length=12, choices=PIE_CHOICES)
    club = models.CharField(max_length=100)  
    valor_mercado = models.DecimalField(max_digits=10, decimal_places=2)
    esta_retirado = models.CharField(max_length=10)  
    valor_mercado_mas_alto = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='jugadores/', blank=True, null=True)

    def __str__(self):
        return self.nombre


class Club(models.Model):
    nombre = models.CharField(max_length=100)
    imagen_escudo = models.ImageField(upload_to='escudos/')
    estadio_nombre = models.CharField(max_length=100)
    estadio_ubicacion = models.CharField(max_length=100)
    valor_plantilla = models.DecimalField(max_digits=12, decimal_places=2)
    capacidad_estadio = models.PositiveIntegerField()
    entrenador = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
