Program ini merupakan implementasi HashMap yang dibuat untuk mensimulasikan sistem penyimpanan data barang pada gudang digital. Fungsi utamanya adalah mengelola data barang menggunakan ID Barang sebagai kunci (key) dan Nama Barang sebagai nilai (value), sehingga proses pencarian data dapat dilakukan dengan cepat dan efisien tanpa harus memeriksa seluruh data yang tersimpan.

Secara teknis, kelas GudangHashMap berfungsi untuk menyimpan data barang ke dalam tabel hash yang terdiri dari dua array, yaitu keys untuk menyimpan ID barang dan values untuk menyimpan nama barang. Metode tambah_barang() digunakan untuk memasukkan data baru ke dalam tabel, sedangkan metode cari_barang() digunakan untuk mencari nama barang berdasarkan ID yang diberikan. Selain itu, metode _hash_function() bertugas menghitung posisi penyimpanan data menggunakan fungsi hash sederhana dengan operasi modulo.

Penjelasan Alur Input & output:
<img width="959" height="539" alt="Screenshot 2026-06-05 191950" src="https://github.com/user-attachments/assets/c19dc0ff-fa8b-4e9f-a614-129a74964afd" />
<img width="959" height="539" alt="Screenshot 2026-06-05 192006" src="https://github.com/user-attachments/assets/9160d173-d0e7-47fe-b680-6afe5451b2fa" />
<img width="959" height="539" alt="Screenshot 2026-06-05 192020" src="https://github.com/user-attachments/assets/47af1b9a-52c5-4be1-9acf-377ebb8809a7" />
<img width="956" height="538" alt="Screenshot 2026-06-05 192039" src="https://github.com/user-attachments/assets/005440df-c066-48ee-8048-f2ee49356c5b" />

Program dimulai dengan membuat objek GudangHashMap yang memiliki kapasitas 5 slot penyimpanan. Pengguna kemudian memasukkan data barang berupa ID barang dan nama barang melalui metode tambah_barang(). Program akan menghitung posisi penyimpanan menggunakan fungsi hash. Jika slot yang dituju kosong, data langsung disimpan. Jika slot sudah terisi (collision), program mencari slot kosong berikutnya menggunakan metode Linear Probing.

Setelah data tersimpan, pengguna dapat mencari barang menggunakan metode cari_barang() dengan memasukkan ID barang. Program menghitung kembali nilai hash dari ID tersebut lalu menelusuri slot yang sesuai hingga data ditemukan. Jika ID ditemukan, program menampilkan nama barang yang terkait. Jika tidak ditemukan, program menampilkan pesan "Barang tidak ditemukan." Dengan cara ini, penyimpanan dan pencarian data dapat dilakukan dengan cepat dan efisien.

Link Youtube: https://youtu.be/feW6z41wFLI?si=D8mi3l6XHpyY2iuX
