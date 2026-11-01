# Pertemuan 12 - File I/O dan Error Handling

Nama: Bilbina Azizi Amarinova  
NIM: 2225250218  
Kelas: 3A

## Tujuan
Membaca, memvalidasi, mengolah, dan menulis data file menggunakan Python serta menangani kesalahan yang mungkin terjadi selama pemrosesan data.

## Format File Input
Data disimpan dalam file teks dengan format NIM dan nilai yang dipisahkan oleh tanda koma.

```text
NIM,nilai
A001,85
A002,78
A003,90
```

## Cara Menjalankan
1. Buka folder proyek di VS Code.
2. Pastikan file input tersedia di folder `data`.
3. Buka terminal VS Code, lalu jalankan perintah:

```bash
python3 tugas/rekap_nilai_file.py
```

## Error yang Ditangani
- **FileNotFoundError:** Terjadi ketika file input tidak ditemukan. Program menampilkan pesan bahwa file tidak ditemukan.
- **ValueError:** Terjadi ketika nilai tidak dapat dikonversi menjadi angka atau format data tidak sesuai. Program menampilkan pesan bahwa data tidak valid.

## Test Case

| Kondisi | Hasil yang Diharapkan | Hasil Aktual | Status |
|---|---|---|---|
| File input berisi data valid | Data dibaca dan rekap berhasil dibuat | Data dibaca dan rekap dibuat | Berhasil |
| File input tidak ditemukan | Program menampilkan pesan kesalahan | Pesan file tidak ditemukan ditampilkan | Berhasil |
| Nilai berisi teks, misalnya `abc` | Data tidak valid ditangani tanpa menghentikan seluruh program | Data tidak valid ditampilkan | Berhasil |
| Terdapat baris kosong | Baris kosong dilewati | Baris kosong dilewati | Berhasil |

## Refleksi
Salah satu error yang ditemukan adalah `ValueError`, yaitu ketika nilai dalam file berisi teks yang tidak dapat dikonversi menjadi angka. Program menangani kesalahan tersebut menggunakan `try-except` sehingga data yang tidak valid dapat dilewati dan proses pembacaan data lainnya tetap berjalan.