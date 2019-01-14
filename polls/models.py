from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Xiencias(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)

class Jjss(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)



class Mcks(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)


class Tipo(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)

class Categoria(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)


class Documento(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)


class Descripcion(models.Model):
    nombre = models.CharField(max_length=1000,blank=True, null=True)
    # equivalencia = models.CharField(max_length=1000,blank=True, null=True)
    # cantidad = models.CharField(max_length=1000,blank=True, null=True)
    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)


class Produccion(models.Model):
    fecha = models.CharField(max_length=1000,blank=True, null=True)
    tipo= models.ForeignKey(Tipo,max_length=1000,blank=True, null=True, related_name='_tipo')
    categoria = models.ForeignKey(Tipo,max_length=1000,blank=True, null=True, related_name='_categoria')
    descripcion = models.ForeignKey(Descripcion,max_length=1000,blank=True, null=True, related_name='_descripcion')
    documento = models.ForeignKey(Documento,max_length=1000,blank=True, null=True, related_name='_documento')
    numero_documento = models.CharField(max_length=1000,blank=True, null=True)
    fecha_emecion = models.CharField(max_length=1000,blank=True, null=True)
    fecha_vencimiento = models.CharField(max_length=1000,blank=True, null=True)
    mes_correspondiente = models.CharField(max_length=1000,blank=True, null=True)
    monto = models.CharField(max_length=1000,blank=True, null=True)
    impuesto = models.CharField(max_length=1000,blank=True, null=True)

    fecha_pago = models.CharField(max_length=1000,blank=True, null=True)
    forma_pago = models.CharField(max_length=1000,blank=True, null=True)
    monto_pagar = models.CharField(max_length=1000,blank=True, null=True)
    estado_desc = models.ForeignKey(Documento,max_length=1000,blank=True, null=True, related_name='_estadodes')
    estado_registro = models.ForeignKey(Documento,max_length=1000,blank=True, null=True, related_name='_estadores')

    # marca = models.CharField(max_length=1000,blank=True, null=True)
    # modelo = models.CharField(max_length=1000,blank=True, null=True)
    # precio = models.CharField(max_length=1000,blank=True, null=True)
    # descuento = models.CharField(max_length=1000,blank=True, null=True)
