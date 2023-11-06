from django.db import models

# Create your models here.
#CharField(max_lenght=20) == varchar(40)
# por el momento todos los campos son obligatorios
# los campos de tipo imagen en la bd se guarda la ruta de la image
# en el projecto te dice upload_to= donde voy a subir
# las imagenes que me estas mandando colocar una carpeta y si
# no hay la crea | creara una carpeta persona a la altura del proyecto
# ydentro de esa carpeta colocamos otra carpeta para que se guarde de
# manera ordenada
# la img se guarda en el projecto y la ruta en la BD


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    descripcion = models.TextField(blank=True, null=True)
    avatar = models.ImageField(
        upload_to='persona/avatar', null=True, blank=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True, unique=True)
    pdf=models.FileField(upload_to='persona/pdf' ,blank=True, null=True)
    # metodo para corregir los estilos de los objetos add a nuestro admin
    # metodo para imprimir los campos de la manera que tu kieres __str__
    # #ordering = ['-nombre'] ordenamiento ascendente  y descentende con -

    def __str__(self):
        # return '{} {}'.format(self.nombre,self.apellido)
        return '{}'.format(self.nombre)

    class Meta:
        verbose_name_plural = 'Persona'
        ordering = ['-nombre']
        
        #db_table = 'Personita'(modifica el nombre de  la tabla de la db)

# persona=models.ForeignKey(Persona,on_delete=models.CASCADE)
# un campo que haga referencia a la clave foreana de la tabla Persona (1=tabla que queremos asociar,2 eliminacion por cascada si se elimina a una persona todos sus campos que esten relacionados en skill tambien seran borrados)


class Skill(models.Model):
    codigo = models.CharField(primary_key=True, max_length=8)
    skill = models.CharField(max_length=20)
    nivel = models.IntegerField()
    estado = models.BooleanField(default=True)
    imagen=models.CharField(max_length=350,blank=True,null=True)
    persona = models.ForeignKey(
    Persona, on_delete=models.CASCADE, blank=True, null=True)
    descripcion=models.TextField(blank=True,null=True)

    def __str__(self):
        return '{}'.format(self.skill)
#ordenar por el campo skill
    class Meta:
        verbose_name_plural = 'Skill'
        ordering=['skill']

#   fecha = models.DateTimeField(auto_now_add=True) conese parametro django coloca automaticamente la fecha del sistema osea ya no colocas nada tu


class Post (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateTimeField()
    imagen = models.ImageField(upload_to='post/imagen', null=True, blank=True)
    estado = models.BooleanField(default=True)
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.titulo)

    class Meta:
        verbose_name_plural = 'Post'
