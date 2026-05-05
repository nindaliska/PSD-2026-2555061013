def binary_search_antrean(daftar_nomor, target):
    low = 0
    high = len(daftar_nomor) - 1
    langkah = 0

    while low <= high:
        langkah += 1
        mid = (low + high) // 2
        tebakan = daftar_nomor[mid]

        print(f"Langkah {langkah}: Mengecek indeks tengah {mid} (Nilai: {tebakan})")

        if tebakan == target:
            return mid, langkah
        if tebakan > target:
            high = mid - 1
        else:
            low = mid + 1
            
    return None, langkah

# Data simulasi: Nomor rekam medis yang sudah terurut
antrean_pasien = [102, 115, 120, 138, 145, 150, 166, 175, 189, 201]

print("--- SISTEM PENCARIAN REKAM MEDIS ---")
print(f"Daftar Antrean: {antrean_pasien}")

target_cari = 189
hasil_indeks, total_langkah = binary_search_antrean(antrean_pasien, target_cari)

if hasil_indeks is not None:
    print(f"\nNomor {target_cari} ditemukan pada urutan ke-{hasil_indeks + 1}")
    print(f"Total pengecekan yang dilakukan: {total_langkah} kali")
else:
    print(f"\nNomor {target_cari} tidak ditemukan dalam daftar.")