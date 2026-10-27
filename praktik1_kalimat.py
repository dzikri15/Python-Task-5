"""Soal Praktik 1 - Analisis Kalimat (String & List)
Modul Pertemuan 5: String, List, Tuple, Set, Dictionary
"""

def analisis_kalimat(kalimat):
    kata = kalimat.split()
    jumlah_kata = len(kata)
    jumlah_karakter = len(kalimat)
    jumlah_karakter_tanpa_spasi = len(kalimat.replace(" ", ""))
    kata_terpanjang = max(kata, key=len) if kata else ""
    kalimat_title = kalimat.title()
    return {
        "jumlah_kata": jumlah_kata,
        "jumlah_karakter": jumlah_karakter,
        "jumlah_karakter_tanpa_spasi": jumlah_karakter_tanpa_spasi,
        "kata_terpanjang": kata_terpanjang,
        "title_case": kalimat_title,
    }


def main():
    kalimat = input("Masukkan sebuah kalimat: ")
    hasil = analisis_kalimat(kalimat)
    print(f"\nKalimat: {kalimat}")
    print(f"(a) Jumlah kata                  : {hasil['jumlah_kata']}")
    print(f"(b) Jumlah karakter (dgn spasi)  : {hasil['jumlah_karakter']}")
    print(f"    Jumlah karakter (tanpa spasi): {hasil['jumlah_karakter_tanpa_spasi']}")
    print(f"(c) Kata terpanjang              : {hasil['kata_terpanjang']}")
    print(f"(d) Title case                  : {hasil['title_case']}")


if __name__ == "__main__":
    main()
