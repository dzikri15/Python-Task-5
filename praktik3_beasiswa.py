"""Soal Praktik 3 - Operasi Himpunan Beasiswa (Set)
Modul Pertemuan 5: String, List, Tuple, Set, Dictionary
"""

# ID mahasiswa penerima beasiswa (data contoh)
beasiswa_a = ["20241320001", "20241320002", "20241320003", "20241320004", "20241320005"]
beasiswa_b = ["20241320004", "20241320005", "20241320006", "20241320007"]


def main():
    set_a = set(beasiswa_a)
    set_b = set(beasiswa_b)

    kedua_beasiswa = set_a & set_b          # irisan
    hanya_a = set_a - set_b                 # selisih A - B
    hanya_b = set_b - set_a                 # selisih B - A
    semua_unik = set_a | set_b              # gabungan

    print(f"Beasiswa A: {sorted(set_a)}")
    print(f"Beasiswa B: {sorted(set_b)}")
    print(f"\n(a) Menerima kedua beasiswa      : {sorted(kedua_beasiswa)}")
    print(f"(b) Hanya menerima beasiswa A    : {sorted(hanya_a)}")
    print(f"(c) Menerima beasiswa B, bukan A : {sorted(hanya_b)}")
    print(f"(d) Semua mahasiswa unik        : {sorted(semua_unik)}")
    print(f"    Total mahasiswa unik         : {len(semua_unik)}")


if __name__ == "__main__":
    main()
