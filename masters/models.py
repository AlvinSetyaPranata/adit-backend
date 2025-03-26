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

class Village(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    subdistrict = models.ForeignKey(Subdistrict, on_delete=models.CASCADE)
    meta = models.JSONField(default=dict)

    class Meta:
        ordering = ['name']

class RegistrationPath(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

class Faculty(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

class StudyProgram(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    code = models.CharField(max_length=10)

    class Meta:
        ordering = ['name']

class RegistrationPeriod(models.Model):
    period = models.CharField(max_length=9, )

    class Meta:
        ordering = ['period']

class School(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    address = models.TextField()
    phone = models.CharField(max_length=15, unique=True)

    class Meta:
        ordering = ['name']

class Job(models.Model):
    job = models.CharField(max_length=100)

    class Meta:
        ordering = ['job']

class Income(models.Model):
    income = models.CharField(max_length=50)

    class Meta:
        ordering = ['income']