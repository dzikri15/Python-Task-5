"""Soal Praktik 4 - Inventaris Toko (Dictionary + Tuple)
Modul Pertemuan 5: String, List, Tuple, Set, Dictionary

Struktur data: nama barang (kunci) -> (harga, stok) sebagai tuple.
"""

# Data awal: nama barang -> (harga_satuan, stok)
inventaris = {
    "Buku Tulis": (15000, 40),
    "Pulpen": (5000, 120),
    "Pensil": (4000, 80),
    "Penghapus": (3000, 60),
}


def tambah_barang(nama, harga, stok):
    """(a) Menambah barang baru. Gagal jika barang sudah ada."""
    if nama in inventaris:
        print(f"Barang '{nama}' sudah ada, tidak ditambahkan.")
        return False
    inventaris[nama] = (harga, stok)
    print(f"Barang '{nama}' ditambahkan: harga Rp{harga}, stok {stok}.")
    return True


def update_stok(nama, stok_baru):
    """(b) Mengupdate stok barang (harga tidak berubah)."""
    if nama not in inventaris:
        print(f"Barang '{nama}' tidak ditemukan.")
        return False
    harga, _ = inventaris[nama]
    inventaris[nama] = (harga, stok_baru)
    print(f"Stok '{nama}' diupdate menjadi {stok_baru}.")
    return True


def cari_harga_range(harga_min, harga_max):
    """(c) Mencari barang dengan harga dalam rentang tertentu."""
    hasil = {nama: v for nama, v in inventaris.items() if harga_min <= v[0] <= harga_max}
    return hasil


def total_nilai_inventaris():
    """(d) Menghitung total nilai inventaris (harga x stok)."""
    return sum(harga * stok for harga, stok in inventaris.values())


def tampilkan_inventaris(judul="Inventaris saat ini:"):
    print(f"\n{judul}")
    for nama, (harga, stok) in inventaris.items():
        print(f"  - {nama}: Rp{harga} x {stok} = Rp{harga * stok}")


def main():
    tampilkan_inventaris()
    print("\n(a) Tambah barang baru:")
    tambah_barang("Penggaris", 10000, 50)
    print("\n(b) Update stok:")
    update_stok("Pulpen", 150)
    print("\n(c) Cari barang dengan harga Rp4.000 - Rp12.000:")
    for nama, (harga, stok) in cari_harga_range(4000, 12000).items():
        print(f"  - {nama}: Rp{harga}, stok {stok}")
    tampilkan_inventaris("Inventaris akhir:")
    print(f"\n(d) Total nilai inventaris: Rp{total_nilai_inventaris()}")


if __name__ == "__main__":
    main()
