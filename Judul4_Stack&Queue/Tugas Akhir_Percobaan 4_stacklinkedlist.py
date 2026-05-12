class Node:
    """Representasi satu 'aksi' atau data dalam Linked List."""
    def __init__(self, data):
        self.data = data
        self.next = None

class UndoStack:
    """Implementasi Stack menggunakan Linked List untuk fitur Undo."""
    def __init__(self):
        self.top = None  # Menunjuk ke elemen teratas (paling baru)
        self._size = 0

    def push(self, action):
        """Menambahkan aksi baru ke tumpukan (Simpan perubahan)."""
        new_node = Node(action)
        new_node.next = self.top
        self.top = new_node
        self._size += 1
        print(f"Menyimpan aksi: '{action}'")

    def pop(self):
        """Mengambil aksi terakhir (Undo)."""
        if self.is_empty():
            print("Tidak ada aksi untuk di-undo.")
            return None
        
        removed_node = self.top
        self.top = self.top.next
        self._size -= 1
        return removed_node.data

    def peek(self):
        """Melihat aksi terbaru tanpa menghapusnya."""
        if self.is_empty():
            return None
        return self.top.data

    def is_empty(self):
        """Mengecek apakah stack kosong."""
        return self.top is None

    def display_stack(self):
        """Menampilkan urutan aksi saat ini di memori."""
        current = self.top
        print("\n--- Riwayat Aksi (Teratas adalah yang terbaru) ---")
        while current:
            print(f"[{current.data}]", end=" -> ")
            current = current.next
        print("None\n")

# --- Simulasi Penggunaan di VS Code ---
editor_history = UndoStack()

# User sedang mengetik...
editor_history.push("Menulis kalimat pertama")
editor_history.push("Menambahkan fungsi main()")
editor_history.push("Menghapus baris ke-10")

editor_history.display_stack()

# User menekan Ctrl + Z (Undo)
print(f"Membatalkan aksi: {editor_history.pop()}")
print(f"Membatalkan aksi: {editor_history.pop()}")

editor_history.display_stack()

# User melihat aksi terakhir yang tersisa
print(f"Aksi saat ini di layar: {editor_history.peek()}")