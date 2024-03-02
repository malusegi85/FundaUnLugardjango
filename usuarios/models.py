from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Usuario autenticación y registro al sistema
 
class Usuario(models.Model):
    nombres=models.CharField(max_length=16, verbose_name="Nombres")
    apellidos=models.CharField(max_length=16, verbose_name="Apellidos")
    foto=models.ImageField(upload_to='images/usuarios',blank=True, default='images/usuarios/default.png')
    email= models.EmailField(max_length=150, verbose_name='Correo')

    class TipoDocumento(models.TextChoices):
        CC='C.C', _('Cédula de Ciudadanía')
        CE='C.E', _('Cédula de Extranjería')
        TI='T.I', _('Tarjeta de Identidad')
        OT='Otro', _('Otro Tipo de Documento')
    tipoDocumento=models.CharField(max_length=4, choices=TipoDocumento.choices, default=TipoDocumento.CC, verbose_name="Tipo de Documento")
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")    
    fecha_nacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")
    

    class Rol(models.TextChoices):
        Administrador='Administrador', _('Administrador')
        Empleado='Empleado', _('Empleado')
        
    rol=models.CharField(max_length=13, choices=Rol.choices, default=Rol.Empleado, verbose_name="Rol")
    class Estado(models.TextChoices):
        ACTIVO='Activo', _('Activo')
        INACTIVO='Inactivo', _('Inactivo')
    estado=models.CharField(max_length=8, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    user=models.ForeignKey(User, on_delete= models.CASCADE)

    def __str__(self)->str:
        return "%s %s" %(self.nombres, self.apellidos)   

# Crea sus modelos aqui

#DATOS BASICOS DEL BENEFICIARIO
class Beneficiario(models.Model):
    documento=models.CharField(max_length=50, verbose_name="Número de Documento") #ESTA ES LA LLAVE PRIMARIA
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        CC='C.C.', _("Cédula de Ciudadania")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos") 
    class Programas(models.TextChoices):
        CUIDARTE='Cuidarte', _("Cuidarte")
        ALIMENTARTE='Alimentarte', _("Alimentarte")
        FORMARTE='Formarte', _("Formarte")
        IMPULSARTE='Impulsarte', _("Impulsarte")
        BIENESTAR='Bienestar', _("Bienestar")
    programas=models.CharField(max_length=20, choices=Programas.choices, verbose_name="Programas")
    genero= models.CharField(max_length=50, verbose_name="Género")     
    class EstadoUsuario(models.TextChoices):
        ACTIVO='Activo', _("Activo")
        INACTIVO='Inactivo', _("Inactivo")
        RETIRADO='Retirado', _("Retirado")
    estadoUsuario=models.CharField(max_length=20, choices=EstadoUsuario.choices, verbose_name="Estado del usuario")   
    fechaNacimiento=models.DateField(verbose_name="Fecha de Nacimiento", help_text=u"MM/DD/AAAA")   
    lugarNacimiento= models.CharField(max_length=50, verbose_name="Lugar de nacimiento")    
    telefono= models.CharField(max_length=50, verbose_name="Teléfono y/o celular") 
          
    def __str__(self):
        return f"{self.nombres} {self.apellidos} {self.documento}"
    
    #AQUI EMPIEZA LOS DATOS DEL ACUDIENTE DEL BENEFICIARIO
class Acudiente(models.Model):
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        CC='C.C.', _("Cédula de Ciudadania")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices,verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres y apellidos")    
    parentesco= models.CharField(max_length=50, verbose_name="Parentesco")
    ocupacion= models.CharField(max_length=50, verbose_name="Ocupación")
    direccion= models.CharField(max_length=50, verbose_name="Dirección") 
    barrio= models.CharField(max_length=50, verbose_name="Barrio y localidad")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    

#AQUI EMPIEZA LOS DATOS DEL PADRINO
class Padrino(models.Model): 
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        CC='C.C.', _("Cédula de Ciudadania")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    correo= models.EmailField(max_length=50, verbose_name="Correo electrónico")  
    ocupacion= models.CharField(max_length=20, verbose_name="Ocupación") #default='ocupacion' .... para agregar campo en el modelo existente, luego se puede borrar      
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    

#AQUI EMPIEZA LAS REFERENCIAS
class Referencia(models.Model):
    documento=models.CharField(max_length=50, verbose_name="Número de Documento")   
    class TipoDocumento(models.TextChoices):
        TI='T.I.', _("Tarjeta de Identidad")
        RC='R.C.', _("Registro Civil")
        CE='C.E.', _("Cédula de Extranjería")
        CC='C.C.', _("Cédula de Ciudadania")
        PASS='PASS', _("Pasaporte")
    tipoDocumento=models.CharField(max_length=5, choices=TipoDocumento.choices, verbose_name="Tipo de Documento")    
    nombres= models.CharField(max_length=50, verbose_name="Nombres")
    apellidos= models.CharField(max_length=50, verbose_name="Apellidos")
    ocupacion= models.CharField(max_length=50, verbose_name="Ocupación")
    relacion= models.CharField(max_length=50, verbose_name="Relación")
    telefono= models.CharField(max_length=50, verbose_name="Teléfono")
    class TipoReferencia(models.TextChoices):
        PER='Personal', _("Personal")
        FAM='Familiar', _("Familiar")
    tipoReferencia=models.CharField(max_length=10, choices=TipoReferencia.choices, verbose_name="Tipo de Referencia")
    beneficiario= models.ForeignKey(Beneficiario, on_delete=models.CASCADE, verbose_name="Beneficiario")
    

