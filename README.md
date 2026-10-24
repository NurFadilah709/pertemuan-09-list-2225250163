# Pertemuan 09 - List/Array dan Pengolahan Data Numerik Sederhana

Nama: Nailah Nur Fadilah 
NIM: 2225250163  
Kelas: 3E  

## Deskripsi

Pertemuan 09 membahas penggunaan **list pada Python** untuk menyimpan dan mengolah data numerik sederhana. Program yang dibuat meliputi pembuatan list, indeks dan slicing, manipulasi list, perhitungan statistik sederhana, filter nilai kelulusan, serta penggunaan fungsi.

## Tujuan

- Memahami penggunaan list pada Python.
- Mengakses elemen list menggunakan indeks dan slicing.
- Memanipulasi data menggunakan `append()`, `insert()`, dan `remove()`.
- Mengolah data menggunakan `sum()`, `len()`, `min()`, dan `max()`.
- Menggunakan perulangan dan percabangan untuk memfilter data.
- Membuat fungsi sederhana untuk mengolah data numerik.

## Struktur Folder

```text
pertemuan-09-list-2225250223/
├── README.md
├── .gitignore
├── latihan/
│   ├── 01_buat_list.py
│   ├── 02_indeks_slicing.py
│   ├── 03_manipulasi_list.py
│   ├── 04_agregasi_nilai.py
│   ├── 05_filter_kelulusan.py
│   └── 06_fungsi_statistik.py
└── praktik/
    └── analisis_nilai_mahasiswa.py
```

## Cara Menjalankan Program

Program dijalankan melalui terminal VS Code menggunakan perintah:

```bash
python latihan/01_buat_list.py
python latihan/02_indeks_slicing.py
python latihan/03_manipulasi_list.py
python latihan/04_agregasi_nilai.py
python latihan/05_filter_kelulusan.py
python latihan/06_fungsi_statistik.py
python praktik/analisis_nilai_mahasiswa.py
```

## Hasil Pengujian Latihan

### Latihan 1 - Membuat List

Program menyimpan lima nilai mahasiswa ke dalam list dan menampilkan jumlah data.

**Hasil:**
```text
[75, 80, 65, 90, 88]
Banyak data = 5
```

### Latihan 2 - Indeks dan Slicing

Program menampilkan elemen pertama, elemen terakhir, tiga elemen awal, serta elemen pada indeks 1 sampai 3.

**Hasil:**
```text
Elemen pertama = 75
Elemen terakhir = 70
Tiga elemen awal = [75, 80, 65]
Indeks 1 sampai 3 = [80, 65, 90]
```

### Latihan 3 - Manipulasi List

Program melakukan perubahan nilai, penambahan data, penyisipan data, dan penghapusan data.

**Hasil:**
```text
List akhir = [75, 70, 82, 90]
```

### Latihan 4 - Agregasi Nilai

Program menghitung total, rata-rata, nilai minimum, dan nilai maksimum.

**Hasil:**
```text
Total = 398
Rata-rata = 79.60
Minimum = 65
Maksimum = 90
```

### Latihan 5 - Filter Kelulusan

Batas kelulusan yang digunakan adalah nilai 60. Nilai yang memenuhi batas tersebut dimasukkan ke dalam list lulus.

**Hasil:**
```text
Nilai lulus = [75, 80, 60, 90]
Jumlah lulus = 4
```

### Latihan 6 - Fungsi Statistik

Program menggunakan fungsi `rata_rata()` untuk menghitung rata-rata. Jika list kosong, fungsi mengembalikan nilai 0 agar program tidak mengalami error.

**Hasil:**
```text
Rata-rata = 79.60
```

## Praktik Analisis Nilai Mahasiswa

Data yang digunakan:

```text
[78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
```

**Hasil:**
```text
Data           : [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
Banyak data    : 10
Total          : 695
Rata-rata      : 69.50
Minimum        : 45
Maksimum       : 90
Nilai lulus    : [78, 90, 67, 60, 82, 71, 88]
Jumlah lulus   : 7
Belum lulus    : 3
```

Program menggunakan dua fungsi, yaitu `rata_rata()` untuk menghitung rata-rata dan `nilai_lulus()` untuk mendapatkan nilai yang memenuhi batas kelulusan.

## Pengujian Kasus

### Kasus 1

Data:

```text
[60, 70, 80]
```

Hasil yang diharapkan:

```text
Rata-rata = 70.00
Minimum = 60
Maksimum = 80
Jumlah lulus = 3
```

### Kasus 2

Data:

```text
[59, 60, 61]
```

Dengan batas kelulusan 60, jumlah nilai yang lulus adalah:

```text
2
```

### Kasus 3

Data kosong:

```text
[]
```

Fungsi `rata_rata()` menghasilkan:

```text
0
```

Program tidak mengalami error ketika menerima list kosong.

## Refleksi

Pada pertemuan ini saya mempelajari cara menggunakan list untuk menyimpan beberapa data dalam satu variabel. Saya juga belajar mengakses data menggunakan indeks dan slicing, memanipulasi list, menghitung statistik sederhana, serta menggunakan perulangan dan percabangan untuk melakukan filter data.

Bagian yang cukup menantang adalah memahami indeks dan slicing serta membuat fungsi yang dapat digunakan kembali. Setelah mencoba menjalankan program melalui terminal VS Code, saya menjadi lebih memahami hubungan antara list, perulangan, fungsi, dan pengolahan data numerik sederhana.

## Kesimpulan

List pada Python dapat digunakan untuk menyimpan dan mengolah banyak data secara lebih praktis. Dengan bantuan fungsi, perulangan, dan percabangan, data dalam list dapat diproses menjadi informasi seperti total, rata-rata, nilai minimum, maksimum, serta data yang memenuhi kriteria tertentu.

## Catatan

Program dibuat dan diuji menggunakan Python melalui Visual Studio Code. Hasil pengujian disesuaikan dengan latihan dan praktik pada bahan ajar Pertemuan 09.