def bubble_sort_antrean(antrean):
    n = len(antrean)
    for i in range(n):
        tukar = False
        for j in range(0, n - i - 1):
            if antrean[j]['jumlah_barang'] > antrean[j+1]['jumlah_barang']:
                antrean[j], antrean[j+1] = antrean[j+1], antrean[j]
                tukar = True
        if not tukar:
            break

pelanggan = [
    {"nama": "Andi", "jumlah_barang": 15},
    {"nama": "Budi", "jumlah_barang": 3},
    {"nama": "Citra", "jumlah_barang": 10},
    {"nama": "Dewi", "jumlah_barang": 1},
    {"nama": "Eko", "jumlah_barang": 7}
]

bubble_sort_antrean(pelanggan)

for p in pelanggan:
    print(f"{p['nama']}: {p['jumlah_barang']} barang")