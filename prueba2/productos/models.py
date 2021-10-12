from django.db import models

# Create your models here.
# modelo para la entidad foto
class Foto(models.Model):
   descripcion=models.CharField(max_length=30)

# modelo para la entidad producto
class Producto(models.Model):
    foto = models.ForeignKey(Foto, null=True, blank=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    precio = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)

# modelo para usuario
class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    correo = models.CharField(max_length=30)
    clave = models.CharField(max_length=30)

# modelo para comentarios
class Comentarios(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    mensaje = models.CharField(max_length=800)

# modelo para carrito
class Carrito(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=30)

# modelo para compra
class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=500)

# modelo para pago
class Pago(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    link_whatsApp = models.CharField(max_length=30)