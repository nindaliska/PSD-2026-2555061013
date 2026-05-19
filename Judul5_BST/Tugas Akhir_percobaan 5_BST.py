class NodeKontak:
    def __init__(self, nama, nomor_hp):
        self.nama = nama
        self.nomor_hp = nomor_hp
        self.kiri = None
        self.kanan = None


class BukuTeleponBST:
    def __init__(self):
        self.root = None

    def tambah_kontak(self, nama, nomor_hp):
        self.root = self._tambah_rekursif(self.root, nama, nomor_hp)

    def _tambah_rekursif(self, node_sekarang, nama, nomor_hp):
        if node_sekarang is None:
            return NodeKontak(nama, nomor_hp)

        if nama.lower() < node_sekarang.nama.lower():
            node_sekarang.kiri = self._tambah_rekursif(node_sekarang.kiri, nama, nomor_hp)
        elif nama.lower() > node_sekarang.nama.lower():
            node_sekarang.kanan = self._tambah_rekursif(node_sekarang.kanan, nama, nomor_hp)
        else:
            node_sekarang.nomor_hp = nomor_hp
            
        return node_sekarang

    def cari_kontak(self, nama):
        return self._cari_rekursif(self.root, nama)

    def _cari_rekursif(self, node_sekarang, nama):
        if node_sekarang is None:
            return None
        
        if nama.lower() == node_sekarang.nama.lower():
            return node_sekarang.nomor_hp
        
        if nama.lower() < node_sekarang.nama.lower():
            return self._cari_rekursif(node_sekarang.kiri, nama)
        
        return self._cari_rekursif(node_sekarang.kanan, nama)

    def tampilkan_semua(self):
        self._in_order_rekursif(self.root)

    def _in_order_rekursif(self, node_sekarang):
        if node_sekarang:
            self._in_order_rekursif(node_sekarang.kiri)
            print(f"- {node_sekarang.nama}: {node_sekarang.nomor_hp}")
            self._in_order_rekursif(node_sekarang.kanan)


if __name__ == "__main__":
    buku_kontak = BukuTeleponBST()

    buku_kontak.tambah_kontak("Budi", "0812-3456-7890")
    buku_kontak.tambah_kontak("Andi", "0856-9999-1111")
    buku_kontak.tambah_kontak("Deni", "0813-2222-3333")
    buku_kontak.tambah_kontak("Citra", "0877-4444-5555")
    buku_kontak.tambah_kontak("Eka", "0899-8888-7777")

    print("=== DAFTAR KONTAK ===")
    buku_kontak.tampilkan_semua()
    print("=====================\n")

    nama_dicari = "Citra"
    hasil = buku_kontak.cari_kontak(nama_dicari)
    
    if hasil:
        print(f"Hasil pencarian '{nama_dicari}': {hasil}")
    else:
        print(f"Kontak '{nama_dicari}' tidak ditemukan.")

    nama_palsu = "Zaki"
    hasil_palsu = buku_kontak.cari_kontak(nama_palsu)
    
    if hasil_palsu:
        print(f"Hasil pencarian '{nama_palsu}': {hasil_palsu}")
    else:
        print(f"Kontak '{nama_palsu}' tidak ditemukan.")