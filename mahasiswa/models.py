from django.db import models
from django.db import models

class Mahasiswa(models.Model):
    nim = models.CharField(max_length=15, unique=True)
    nama = models.CharField(max_length=100)
    programstudi = models.CharField(max_length=50)
    angkatan = models.CharField(max_length=4) 

    def __str__(self):
        return f"{self.nim} - {self.nama}"
