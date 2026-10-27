"""Soal Praktik 2 - Analisis Nilai Mahasiswa (List & Dictionary)
Modul Pertemuan 5: String, List, Tuple, Set, Dictionary

Skala kategori mengikuti studi kasus modul (Bab 6.4):
A >= 85, B >= 70, C >= 55, D >= 40, E < 40
"""


def kategori(nilai):
    if nilai >= 85:
        return "A"
    if nilai >= 70:
        return "B"
    if nilai >= 55:
        return "C"
    if nilai >= 40:
        return "D"
    return "E"


def analisis_nilai(nilai_list):
    rata_rata = sum(nilai_list) / len(nilai_list)
    tertinggi = max(nilai_list)
    terendah = min(nilai_list)
    frekuensi = {}
    for nilai in nilai_list:
        kat = kategori(nilai)
        frekuensi[kat] = frekuensi.get(kat, 0) + 1
    return rata_rata, tertinggi, terendah, frekuensi


def main():
    raw = input("Masukkan nilai mahasiswa (pisahkan dengan koma): ")
    nilai_list = [float(x.strip()) for x in raw.split(",") if x.strip()]
    rata_rata, tertinggi, terendah, frekuensi = analisis_nilai(nilai_list)
    print(f"\nDaftar nilai: {nilai_list}")
    print(f"(a) Rata-rata        : {rata_rata:.2f}")
    print(f"(b) Nilai tertinggi  : {tertinggi}")
    print(f"    Nilai terendah   : {terendah}")
    print("(c) Kategori tiap nilai:")
    for nilai in nilai_list:
        print(f"    - {nilai} -> {kategori(nilai)}")
    print("(d) Frekuensi tiap kategori:")
    for kat in ["A", "B", "C", "D", "E"]:
        print(f"    - {kat}: {frekuensi.get(kat, 0)}")


if __name__ == "__main__":
    main()
