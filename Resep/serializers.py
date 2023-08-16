from rest_framework import serializers
from .models import Resep,Bahan, Kategori


class TakaranSerializer(serializers.Serializer):
    bahan = serializers.CharField()
    takaran = serializers.CharField(required=False, allow_blank=True)

class ResepSerializer(serializers.ModelSerializer):
    bahan = serializers.SerializerMethodField()
    kategori = serializers.StringRelatedField(source='id_kategori.nama_kategori')
    class Meta:
        model = Resep
        fields = ['id','nama_resep','bahan','kategori']

    def get_bahan(self, obj):
        
        return [b.nama_bahan for b in obj.id_bahan.all()]

class BahanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bahan
        fields = "__all__"

class KategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kategori
        fields = "__all__"