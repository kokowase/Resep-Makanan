from django import forms
from .models import Resep, Bahan, Kategori

class ResepForm(forms.ModelForm):
    id_bahan = forms.ModelMultipleChoiceField(queryset=Bahan.objects.all(), widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Resep
        fields = ['id_kategori','id_bahan','nama_resep']
        


class BahanForm(forms.ModelForm):
    class Meta:
        model = Bahan
        fields = "__all__"

class KategoriForm(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = "__all__"