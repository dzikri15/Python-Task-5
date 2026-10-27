"""Soal Praktik 5 - Analisis Frekuensi Kata dari File (String, List, Set, Dict)
Modul Pertemuan 5: String, List, Tuple, Set, Dictionary
"""

import re
from collections import Counter

FILE_TEKST = "data/contoh_teks.txt"


def baca_kata(path):
    with open(path, "r", encoding="utf-8") as f:
        teks = f.read()
    # Huruf kecil semua, hanya huruf/angka yang dihitung sebagai kata
    kata = re.findall(r"[a-z0-9]+", teks.lower())
    return kata


def main():
    kata = baca_kata(FILE_TEKST)
    frekuensi = Counter(kata)
    total_kata = len(kata)
    kata_unik = set(kata)

    print(f"File: {FILE_TEKST}")
    print(f"Total kata: {total_kata}")
    print(f"Jumlah kata unik: {len(kata_unik)}")

    print("\n(a) Frekuensi setiap kata:")
    for k, v in sorted(frekuensi.items()):
        print(f"  - {k}: {v}")

    print("\n(b) 10 kata paling sering muncul:")
    for k, v in frekuensi.most_common(10):
        print(f"  - {k}: {v}")

    hapax = sorted(k for k, v in frekuensi.items() if v == 1)
    print(f"\n(c) Kata yang hanya muncul sekali (hapax legomena, {len(hapax)} kata):")
    print(f"  {', '.join(hapax)}")

    ttr = len(kata_unik) / total_kata if total_kata else 0
    print(f"\n(d) Type-token ratio (kata unik / total kata): {ttr:.4f}")


if __name__ == "__main__":
    main()
