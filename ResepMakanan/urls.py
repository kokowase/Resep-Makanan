"""ResepMakanan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Resep import views as r_views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('bahan',r_views.BahanView)
router.register('kategori',r_views.KategoriView)
router.register('resep',r_views.ResepView)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('',r_views.home,name="home"),
    path('buat_kategori',r_views.buat_kategori,name="buat_kategori"),
    path('buat_resep',r_views.buat_resep,name="buat_resep"),
    path('buat_bahan',r_views.buat_bahan,name="buat_bahan"),
    path('detail_resep/<id_resep>',r_views.detail_resep,name="detail_resep"),

]
