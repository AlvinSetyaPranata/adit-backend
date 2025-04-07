from django.db import models
from masters.models import (Religion, Gender, Citizen, Province, Regency, Subdistrict, Village, RegistrationPath, Faculty, StudyProgram, RegistrationPeriod, School, Job, Income)

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    nik = models.CharField(max_length=16, unique=True)
    kk = models.CharField(max_length=16, unique=True)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    # education = models.ForeignKey(Education, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    income = models.ForeignKey(Income, on_delete=models.PROTECT)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name if self.last_name else ''} ({self.nik})"

class Calon_mahasiswa(models.Model):
    code = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    religion = models.ForeignKey(Religion, on_delete=models.CASCADE)
    citizen = models.ForeignKey(Citizen, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    regency = models.ForeignKey(Regency, on_delete=models.CASCADE)
    subdistrict = models.ForeignKey(Subdistrict, on_delete=models.CASCADE)
    village = models.ForeignKey(Village, on_delete=models.CASCADE)
    registrationpath = models.ForeignKey(RegistrationPath, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)
    studyprogram = models.ForeignKey(StudyProgram, on_delete=models.CASCADE)
    registrationperiod = models.ForeignKey(RegistrationPeriod, on_delete=models.CASCADE)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    parent = models.ForeignKey(Parent, on_delete=models.CASCADE)

    class Meta:
        ordering = ['code']
        
    def __str__(self):
        return f"{self.code} - {self.first_name} {self.last_name or ''}"