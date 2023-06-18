from django.db import models


class TypeOfProduct(models.Model):
    type = models.CharField(max_length=70)

    def __str__(self):
        return self.type
    objects = models.Model


class Producer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    objects = models.Model


class Product(models.Model):
    type = models.ForeignKey(TypeOfProduct, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.PROTECT)
    count = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение')

    def __str__(self):
        return self.name
    objects = models.Model
