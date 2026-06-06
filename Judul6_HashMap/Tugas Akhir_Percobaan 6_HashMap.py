class GudangHashMap:
    def __init__(self, kapasitas):
        self.kapasitas = kapasitas
        self.size = 0
        # Inisialisasi tabel dengan None
        self.keys = [None] * kapasitas
        self.values = [None] * kapasitas

    def _hash_function(self, key):
        # Menggunakan fungsi modulo sederhana
        return hash(key) % self.kapasitas

    def tambah_barang(self, id_barang, nama_barang):
        if self.size == self.kapasitas:
            print("Gudang Penuh!")
            return

        index = self._hash_function(id_barang)

        # Open Addressing: Linear Probing
        # Jika index sudah terisi, cari index selanjutnya secara berurutan
        while self.keys[index] is not None:
            if self.keys[index] == id_barang:  # Update jika ID sudah ada
                self.values[index] = nama_barang
                return
            index = (index + 1) % self.kapasitas

        self.keys[index] = id_barang
        self.values[index] = nama_barang
        self.size += 1
        print(f"Barang '{nama_barang}' berhasil disimpan di slot {index}")

    def cari_barang(self, id_barang):
        index = self._hash_function(id_barang)
        start_index = index

        while self.keys[index] is not None:
            if self.keys[index] == id_barang:
                return self.values[index]
            
            index = (index + 1) % self.kapasitas
            
            # Jika kembali ke titik awal, berarti tidak ditemukan
            if index == start_index:
                break
        
        return "Barang tidak ditemukan."

# --- Uji Coba Studi Kasus ---
gudang = GudangHashMap(kapasitas=5)

# Menambahkan data barang
gudang.tambah_barang("A1", "Laptop ASUS")
gudang.tambah_barang("B2", "Mouse Logi")
gudang.tambah_barang("C3", "Keyboard Mech")

# Simulasi Tabrakan (Collision)
# Jika ID "D4" menghasilkan hash yang sama dengan salah satu di atas
gudang.tambah_barang("D4", "Monitor 4K")

print("\n--- Hasil Pencarian ---")
print(f"Cari ID 'B2': {gudang.cari_barang('B2')}")
print(f"Cari ID 'Z9': {gudang.cari_barang('Z9')}")