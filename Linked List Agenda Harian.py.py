class Kegiatan:
    def __init__(self, nama, jam):
        self.nama = nama
        self.jam = jam
        self.next = None

class AgendaHarian:
    def __init__(self):
        self.head = None

    def tambah(self, nama, jam):
        baru = Kegiatan(nama, jam)
        if not self.head:
            self.head = baru
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = baru

    def cetak_semua(self):
        skrg = self.head
        while skrg:
            print(f"{skrg.jam}: {skrg.nama}")
            skrg = skrg.next

# Inisialisasi langsung
jadwal = AgendaHarian()
jadwal.tambah("Bangun Tidur", "05:00")
jadwal.tambah("Sarapan", "07:00")
jadwal.tambah("Belajar Python", "08:00")
jadwal.cetak_semua()