from django.db import models

# Create your models here.
from django.contrib.auth.decorators import login_required
from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


class UserManager(BaseUserManager,models.Manager):
    def _create_user(self,usu_cedula,usu_nombre,usu_correo,password,is_staff,
                    is_superuser,**extra_fields):
        usu_correo=self.normalize_email(usu_correo)
        if not usu_correo:
            raise ValueError('El email debe ser Obligatorio!')
        user = self.model(usu_cedula=usu_cedula,usu_nombre=usu_nombre,usu_correo=usu_correo,is_staff=is_staff,
                            is_active=True,is_superuser=is_superuser,**extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,usu_cedula,usu_nombre,usu_correo,password=None,**extra_fields):
        return self._create_user(usu_cedula,usu_nombre,usu_correo,password,False,False,**extra_fields)

    def create_superuser(self,usu_cedula,usu_nombre,usu_correo,password=None,**extra_fields):
        return self._create_user(usu_cedula,usu_nombre,usu_correo,password,True,True,**extra_fields)




class Proveedor (models.Model):

    prov_cedula = models.CharField(primary_key=True,max_length = 10)
    prov_repre = models.CharField(max_length = 50)
    prov_direccion = models.CharField(max_length = 80)
    prov_ciudad = models.CharField(max_length = 30)
    prov_telefono = models.CharField(max_length = 25)
    prov_nombre = models.CharField(max_length = 50)
    prov_correo = models.EmailField()
    EST_CHOICES = (
            (u'a', u'Activo'),
            (u'i', u'Inactivo'),
    )

    prov_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='a')
    def __unicode__(self):
        return self.prov_nombre

class Categoria (models.Model):
    cat_id = models.AutoField(primary_key=True)
    cat_nombre = models.CharField(max_length = 50)
    cat_detalle = models.CharField(max_length = 80)
    EST_CHOICES = (
            (u'a', u'Activo'),
            (u'i', u'Inactivo'),
    )

    cat_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='a')
    def __unicode__(self):
        return self.cat_nombre


class Producto (models.Model):
    prov_cedula = models.ForeignKey(Proveedor)
    cat_id = models.ForeignKey(Categoria)
    pro_id = models.AutoField(primary_key=True)
    pro_nombre = models.CharField(max_length = 50)
    pro_modelo = models.CharField(max_length = 50)
    pro_marca = models.CharField(max_length = 50)
    pro_stocka = models.CharField(max_length = 10,default='0')
    pro_stockm = models.CharField(max_length = 10,default='0')
    pro_precio = models.FloatField()
    pro_preciov = models.FloatField()
    EST_CHOICES = (
            (u'a', u'Activo'),
            (u'i', u'Inactivo'),
    )

    pro_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='a')

class Rol (models.Model):
    rol_id = models.AutoField(primary_key=True)
    rol_nombre = models.CharField(max_length = 30)
    rol_detalle = models.CharField(max_length = 50)


class Permiso (models.Model):
    rol_id = models.ForeignKey(Rol)
    per_id = models.AutoField(primary_key=True)
    per_nombre = models.CharField(max_length = 30)
    per_detalle = models.CharField(max_length = 50)

class Usuario (AbstractBaseUser,PermissionsMixin):

    usu_cedula = models.CharField(primary_key=True,max_length = 10)
    usu_nombre = models.CharField(max_length = 20)
    usu_apellido = models.CharField(max_length = 50)
    usu_correo = models.EmailField()

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    EST_CHOICES = (
            (u'a', u'Activo'),
            (u'i', u'Inactivo'),
    )

    usu_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='a')

    object=UserManager()

    USERNAME_FIELD = 'usu_cedula'
    REQUIRED_FIELDS = ['usu_correo','usu_nombre']
    def get_short_name(self):
        return self.usu_nombre

class Cliente (models.Model):
    cli_cedula = models.CharField(primary_key=True,max_length = 10)
    cli_nombre = models.CharField(max_length = 30)
    cli_apellido = models.CharField(max_length = 30)
    cli_telefono = models.CharField(max_length = 20)
    cli_direccion = models.CharField(max_length = 80)
    cli_ciudad = models.CharField(max_length = 30)
    EST_CHOICES = (
            (u'a', u'Activo'),
            (u'i', u'Inactivo'),
    )

    cli_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='a')


class OrdenTrabajo (models.Model):
    cli_cedula = models.ForeignKey(Cliente)
    ord_id = models.AutoField(primary_key=True)
    ord_numero = models.CharField(max_length=20)
    ord_fechar = models.DateField(default=date.today)
    ord_fechae = models.DateField(default=date.today)
    ord_detalle = models.CharField(max_length = 90)
    ord_servicio = models.CharField(max_length = 90,default='')
    ord_precio = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    ord_tipo = models.CharField(max_length = 20)
    EST_CHOICES = (
            (u'h', u'Habilitada'),
            (u'a', u'Anulada'),
            (u'f', u'Finalizada'),
    )

    ord_estado = models.CharField(max_length = 1, choices=EST_CHOICES, default='h')


class OrdenProducto (models.Model):
    ord_id = models.ForeignKey(OrdenTrabajo)
    pro_id = models.ForeignKey(Producto)
    ordp_cantidad = models.DecimalField(decimal_places=2,max_digits=8,default=0)
    ordp_precio = models.DecimalField(decimal_places=2,max_digits=8,default=0)

