from django.test import TestCase
from django.urls import reverse
from .models import Kategori, Bahan, Resep
from .forms import ResepForm
# Create your tests here.


class ResepTestCase(TestCase):

    def setUp(self):
        self.kategori = Kategori.objects.create(nama_kategori='Main Course')
        self.bahan = Bahan.objects.create(nama_bahan='Bawang Putih')
        self.resep = Resep.objects.create(id_kategori=self.kategori,nama_resep='Bawang Putih')
        self.resep.id_bahan.add(self.bahan)
        self.url_buat_bahan = reverse('buat_bahan')
        self.url_buat_kategori = reverse('buat_kategori')
        self.url_buat_resep = reverse('buat_resep')
        self.url_home = reverse('home')
        self.url_detail_resep = reverse('detail_resep', args=[self.resep.id])

    def test_buat_bahan_view(self):
        response = self.client.get(self.url_buat_bahan)
        self.assertEqual(response.status_code, 200)

        response = self.client.post(self.url_buat_bahan, {'nama_bahan': 'Bawang Merah'})
        self.assertEqual(response.status_code, 302)
    
    def test_buat_kategori_view(self):
        response = self.client.get(self.url_buat_kategori)
        self.assertEqual(response.status_code,200)

        response = self.client.post(self.url_buat_kategori, {'nama_kategori': 'Dessert'})
        self.assertEqual(response.status_code, 302)

    def test_buat_resep_view(self):
        response = self.client.get(self.url_buat_resep)
        self.assertEqual(response.status_code, 200)

        id_bahan = [self.bahan.id]  # Ganti ini dengan ID bahan yang benar
        response = self.client.post(self.url_buat_resep, {'id_kategori': self.kategori.id, 'id_bahan': id_bahan, 'nama_resep': 'Nasi Goreng'})
        self.assertEqual(response.status_code, 302)
    
    def test_home(self):
        response = self.client.get(self.url_home)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Resep/home.html')
        self.assertContains(response, 'resep')

    def test_detail_resep_view(self):
        response = self.client.get(self.url_detail_resep)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Resep/DetailResep.html')
        self.assertContains(response, self.resep.nama_resep)  
        self.assertContains(response, self.bahan.nama_bahan)



