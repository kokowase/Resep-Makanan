from django.db import models

# Create your models here.

class Kategori(models.Model):
    nama_kategori = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.nama_kategori
    
class Bahan(models.Model):
    nama_bahan = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.nama_bahan
    
class Resep(models.Model):
    id_kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE)
    id_bahan = models.ManyToManyField(Bahan)
    nama_resep = models.CharField(max_length=128,null=True,blank=True)
   