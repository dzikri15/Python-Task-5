# Soal Teori — Pertemuan 5: String, List, Tuple, Set, Dictionary

## 1. Perbedaan List dan Tuple

Perbedaan mendasarnya adalah **mutabilitas**: list bersifat **mutable** (isi, urutan, dan
ukurannya bisa diubah setelah dibuat), sedangkan tuple bersifat **immutable** (tidak bisa
diubah setelah dibuat). Konsekuensinya, list punya metode mutasi seperti `append()`,
`insert()`, `remove()`, dan `pop()`, sedangkan tuple hanya punya `count()` dan `index()`
yang bersifat read-only. Karena immutable, tuple bersifat hashable sehingga bisa dipakai
sebagai kunci dictionary atau elemen set; list tidak bisa.

- **Tuple lebih tepat** untuk data yang tidak boleh berubah dan bermakna tetap, misalnya
  koordinat `(lat, lon)`, tanggal `(tahun, bulan, hari)`, konfigurasi tetap, atau nilai
  kembalian fungsi yang terdiri dari beberapa nilai.
- **List lebih tepat** untuk koleksi yang berubah selama program berjalan, misalnya daftar
  nama mahasiswa yang bisa bertambah, antrean tugas, atau hasil query database yang perlu
  diurutkan dan difilter.

## 2. Mengapa Set Tidak Mendukung Pengindeksan?

Set diimplementasikan dengan **hash table**: setiap elemen disimpan pada posisi yang
ditentukan oleh nilai hash-nya, bukan berdasarkan urutan penyisipan. Karena itu set
bersifat **unordered** — tidak ada konsep "elemen ke-0" atau "elemen ke-3" yang stabil.
Pengindeksan seperti `s[0]` menjadi tidak bermakna, sebab elemen yang didapat pada
indeks tertentu tidak bisa dijamin sama antar eksekusi. Untuk mengakses elemen set,
digunakan iterasi atau pengujian keanggotaan (`in`), bukan indeks.

## 3. Hashable dalam Python

**Hashable** artinya suatu objek memiliki nilai hash yang tetap selama masa hidupnya dan
mendukung perbandingan kesetaraan, sehingga bisa disimpan di hash table (set dan
dictionary). Nilai hash inilah yang dipakai untuk menentukan posisi penyimpanan dan
pencarian cepat.

- **Hashable:** `int`, `str`, `tuple` (jika semua elemennya hashable).
- **Tidak hashable:** `list`, `dict`, `set` (karena mutable — isinya bisa berubah,
  sehingga nilai hash-nya tidak bisa dijamin tetap).

Kunci dictionary **harus hashable** karena dictionary mencari nilai lewat hash kunci
tersebut. Kalau kunci bisa berubah isinya (seperti list), hash-nya berubah, dan dictionary
tidak akan bisa menemukan lagi nilai yang disimpan di bawah kunci itu.

## 4. Keanggotaan O(1) pada Set vs O(n) pada List

Pada set, operator `in` menghitung hash dari nilai yang dicari lalu langsung menuju
posisi penyimpanannya di hash table — rata-rata **O(1)**, tidak peduli berapa banyak
elemennya. Pada list, tidak ada peta posisi: Python harus memeriksa elemen satu per satu
dari awal sampai ketemu (atau sampai habis) — **O(n)**.

Implikasi praktisnya besar untuk data besar: misalnya memeriksa apakah 10.000 NIM sudah
terdaftar. Dengan list berisi 1.000.000 NIM, tiap pengecekan bisa memindai hingga
1.000.000 elemen; dengan set, tiap pengecekan praktis instan. Karena itu, untuk validasi,
filtering, dan deduplikasi data besar, ubah dulu koleksinya menjadi set.

## 5. Perbedaan `sort()` dan `sorted()`

| Aspek | `list.sort()` | `sorted(list)` |
|---|---|---|
| Jenis | Metode list | Fungsi bawaan |
| Hasil | Mengurutkan **in-place** (list asli berubah), mengembalikan `None` | Mengembalikan **list baru** yang terurut, list asli tidak berubah |
| Berlaku untuk | Hanya list | Iterable apa pun (list, tuple, set, dict) |

Gunakan `sort()` ketika list asli memang sudah boleh diubah dan tidak diperlukan lagi
versi tak terurutnya (lebih hemat memori). Gunakan `sorted()` ketika urutan asli harus
dipertahankan, atau ketika sumber datanya bukan list (misalnya mengurutkan set atau
nilai-nilai dictionary).
