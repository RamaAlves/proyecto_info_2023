from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Noticia(models.Model):
    titulo = models.CharField(max_length=30)
    resumen = models.CharField(max_length=100)
    contenido = models.TextField()
    fecha_de_publicacion = models.DateTimeField(auto_now_add=True)
    #Para usar imagenes debemos instalar pillow
    imagen = models.ImageField(upload_to='noticias')
    categoria_noticia = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo