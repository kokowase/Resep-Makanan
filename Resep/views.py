from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Resep, Bahan, Kategori
from .forms import ResepForm, BahanForm, KategoriForm
from .serializers import ResepSerializer, BahanSerializer, KategoriSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from django_filters import rest_framework as filters


# Create your views here.

def home(request):
    resep = Resep.objects.all()
    context= {
        'resep':resep
    }
    return render(request, 'Resep/home.html',context)

def buat_bahan(request):
    form = BahanForm()
    if request.method == 'POST':
        form = BahanForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Bahan Berhasil dibuat')
            return redirect('home')
            
    context = {
        'form':form
    }
    return render(request, 'Resep/BuatBahan.html', context)

def buat_kategori(request):
    form = KategoriForm()
    if request.method == 'POST':
        form = KategoriForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Kategori Berhasil dibuat')
            return redirect('home')
    context = {
        'form':form
    }
    return render(request, 'Resep/BuatKategori.html', context)

def buat_resep(request):
    form = ResepForm()
    if request.method == 'POST':
        form = ResepForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Resep Berhasil dibuat')
            print("Redirecting to home...")
            return redirect('home')
    
    context = {
        'form':form
    }
    return render(request, 'Resep/BuatResep.html', context)

def detail_resep(request,id_resep):
    resep = Resep.objects.get(id=id_resep)

    context={
        'resep':resep
    }
    return render(request, 'Resep/DetailResep.html', context)

class BahanView(viewsets.ModelViewSet):
    queryset = Bahan.objects.all()
    serializer_class = BahanSerializer

class KategoriView(viewsets.ModelViewSet):
    queryset = Kategori.objects.all()
    serializer_class = KategoriSerializer

class ResepFilter(filters.FilterSet):
    nama_bahan = filters.CharFilter(field_name='id_bahan__nama_bahan', lookup_expr='icontains')
    nama_kategori = filters.CharFilter(field_name='id_kategori__nama_kategori', lookup_expr='icontains')

    class Meta:
        model = Resep
        fields = ['nama_bahan', 'nama_kategori', 'nama_resep']

class ResepView(viewsets.ModelViewSet):
    queryset = Resep.objects.all()
    serializer_class = ResepSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ResepFilter