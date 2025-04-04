from django.db import models
from masters.models import (Religion, Gender, Citizen, Province, Regency, Subdistrict, Village, RegistrationPath, Faculty, StudyProgram, RegistrationPeriod, School, Job, Income)

class Parent(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    nik = models.CharField(max_length=16)
    kk = models.CharField(max_length=16)
    address = models.TextField()
    contact = models.CharField(max_length=15)
    # education = models.ForeignKey(Education, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)
    income = models.ForeignKey(Income, on_delete=models.PROTECT)

    class Meta:
        ordering = ['first_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name if self.last_name else ''} ({self.nik})"