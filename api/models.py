from django.db import models

class Usuario(models.Model):
    ESTADO_CHOICES = [
        ('activo', 'Activo'),
        ('suspendido', 'Suspendido')
    ]
    user_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    foto_id = models.BinaryField(null=True)
    foto_perfil = models.BinaryField(null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default='activo')

    def __str__(self):
        return self.nombre

class PerfilDeUsuario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total_reportes = models.IntegerField(default=0)
    total_apoyos = models.IntegerField(default=0)

    def __str__(self):
        return f"Perfil de {self.usuario.nombre}"

class EntidadOficial(models.Model):
    entidad_id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50, null=True)
    url_oficial = models.URLField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

class Reporte(models.Model):
    ESTADO_REPORTE_CHOICES = [
        ('abierto', 'Abierto'),
        ('en progreso', 'En Progreso'),
        ('cerrado', 'Cerrado')
    ]
    reporte_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_reporte = models.DateTimeField(auto_now_add=True)
    ubicacion_latitud = models.FloatField(null=True)
    ubicacion_longitud = models.FloatField(null=True)
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField(null=True)
    foto_reporte = models.BinaryField(null=True)
    foto_referencia = models.BinaryField(null=True)
    estado_reporte = models.CharField(max_length=20, choices=ESTADO_REPORTE_CHOICES, default='abierto')
    entidad = models.ForeignKey(EntidadOficial, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Reporte {self.reporte_id}"

class ApoyoEnReporte(models.Model):
    apoyo_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    fecha_apoyo = models.DateTimeField(auto_now_add=True)

class ComentarioEnReporte(models.Model):
    comentario_id = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    reporte = models.ForeignKey(Reporte, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)
