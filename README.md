# Resep-Makanan

## Deskripsi

Proyek ini merupakan bagian dari sebuah tantangan teknis dalam proses interview. 
Tujuannya adalah untuk membuat sebuah API yang memungkinkan pengguna untuk menyimpan, mengambil, mengupdate, dan menghapus resep makanan.
Proyek ini juga memperlihatkan penggunaan data master bahan dan kategori.

## Fitur
-API CRUD untuk data master (bahan dan kategori)
-API CRUD data Resep
-API CRUD menampilkan lis/index berdasarkan filter bahan dan kategori

# Dokumentasi API

1. Resep
  Endpoint: /api/resep/
  - Daftar Resep
    GET /api/resep/
  - Tambah Resep Baru
    POST /api/resep/
  - Detail Resep berdasarkan id
    GET /api/resep/{id}/
  - Update Resep
    PUT /api/resep/{id}/
  - Hapus Resep
    DELETE /api/resep/{id}/
2. Bahan
   Endpoint: /api/bahan/
    - Daftar bahan
      GET /api/bahan/
    - Tambah nahan Baru
      POST /api/bahan/
    - Detail bahan berdasarkan id
      GET /api/bahan/{id}/
    - Update Bahan
      PUT /api/bahan/{id}/
    - Hapus Bahan
      DELETE /api/bahan/{id}/
3. Kategori
   Endpoint: /api/kategori/
    - Daftar Kategori
      GET /api/kategori/
    - Tambah Resep Kategori
      POST /api/kategori/
    - Detail Kategori berdasarkan id
      GET /api/kategori/{id}/
    - Update Kategori
      PUT /api/kategori/{id}/
    - Hapus Kategori
      DELETE /api/kategori/{id}/
4. Penggunaan Filter dan Pencarian Resep berdasarkan kategori dan bahan
   Parameter Query:
    - nama_bahan: Filter resep berdasarkan nama bahan yang digunakan.
    - nama_kategori: Filter resep berdasarkan nama kategori.
    - nama_resep: Filter resep berdasarkan nama resep.
      - GET /api/resep/?nama_bahan=telor
      JSON Response:
                    {
        "id": 2,
        "nama_resep": "Nasi Telor Spesial",
        "bahan": [
            "Bawang Putih",
            "Bawang Merah",
            "Minyak",
            "Nasi Putih",
            "Daun Bawang",
            "Telor 2"
          ],
            "kategori": "Main Course"
        }
     - GET /api/resep/?nama_kategori=main
       JSON Response:
       {
        "id": 2,
        "nama_resep": "Nasi Telor Spesial",
        "bahan": [
            "Bawang Putih",
            "Bawang Merah",
            "Minyak",
            "Nasi Putih",
            "Daun Bawang",
            "Telor 2"
          ],
            "kategori": "Main Course"
        }
    - GET /api/resep/?nama_resep=nasi telor
      JSON Response:
       {
        "id": 2,
        "nama_resep": "Nasi Telor Spesial",
        "bahan": [
            "Bawang Putih",
            "Bawang Merah",
            "Minyak",
            "Nasi Putih",
            "Daun Bawang",
            "Telor 2"
          ],
            "kategori": "Main Course"
        }
    Jika ingin menggunakan parameter lebih dari satu maka gunakan "&" diantara parameter
    - GET /api/resep/?nama_resep=nasi telor&nama_bahan=minyak&nama_kategori=main
  

    



