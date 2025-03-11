from django.db import models

# Create your models here.
class Religion(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

class Gender(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']


class Citizen(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

class Province(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

class Regency(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

class Subdistrict(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']