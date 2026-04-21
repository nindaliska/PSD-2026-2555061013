Fungsi utama program ini sebenarnya buat jadi semacam pengatur jadwal otomatis yang bikin urutan kegiatan jadi lebih rapi dan nyambung satu sama lain. Tiap aktivitas dibikin kayak punya "tali" buat narik aktivitas selanjutnya, jadi urutan hari-hari nggak bakal ketuker. Pakai cara ini, nambahin agenda baru di tengah-tengah jadwal jadi jauh lebih gampang dan fleksibel karena tinggal mindahin pengaitnya aja tanpa perlu ngerombak seluruh daftar dari awal.

Selain itu, program ini juga berfungsi buat nunjukin cara kerja data yang "jalan" berurutan dari pagi sampai malam. Sistem bakal ngecek satu-satu mulai dari kegiatan paling pertama, lalu ngikutin petunjuk ke kegiatan berikutnya sampai semua jadwal beres dibaca. Jadi, tujuan akhirnya bukan cuma buat nyimpen daftar tugas, tapi buat mastiin alur kegiatan harian tersusun rapi secara kronologis dan nggak ada agenda yang kelewat.

Penjelasan Alur Input & output:
<img width="1917" height="1077" alt="Screenshot 2026-04-20 195023" src="https://github.com/user-attachments/assets/785b3f4c-4349-4cfb-b0d1-83a86b0c13cd" />
<img width="1915" height="1043" alt="Screenshot 2026-04-20 195044" src="https://github.com/user-attachments/assets/a3ce4b96-9f9b-4d93-aa05-a3e1df2d2c0d" />
<img width="1849" height="907" alt="Screenshot 2026-04-20 195147" src="https://github.com/user-attachments/assets/a59c35fe-2a29-42c8-9d6e-b27d992da9c9" />

Bayangin kode ini lagi bikin barisan orang atau antrean gitu. Pertama, ada class Kegiatan yang tugasnya bikin "identitas" tiap orang, isinya ada jam, nama acara, sama tangan buat gandeng orang di belakangnya.
Terus ada class AgendaHarian yang jadi koordinatornya. Waktu pertama kali dibuat, antreannya masih kosong melompong. Pas fungsi tambah dipanggil buat masukin jadwal kayak "Bangun Tidur", "Sarapan", sama "Belajar Python", si koordinator ini bakal ngecek: kalau barisan masih kosong, orang pertama langsung berdiri paling depan. Tapi kalau udah ada orangnya, program bakal nyari siapa yang berdiri paling ujung belakang, terus nyuruh orang baru itu buat gandengan di sana. Itu sebabnya semua jadwal kamu bisa nyambung satu sama lain.
Pas semua udah beres dan fungsi cetak_semua dipanggil, di situlah Output nongol di terminal. Si program bakal absen satu-satu dari orang paling depan sampai paling belakang. Sambil jalan, dia bakal nyebutin jam sama nama kegiatannya.
Hasil akhirnya di terminal bakal kelihatan kayak gini:
05:00: Bangun Tidur
07:00: Sarapan
08:00: Belajar Python
Urutannya beneran rapi sesuai siapa yang masuk duluan karena sistemnya emang naruh yang baru di paling belakang. Formatnya juga 
asik dilihat karena kodenya udah disetel buat nampilin jam dulu, baru deh nama acaranya.

Link Youtube: https://youtu.be/pFcEPrD_4NY?si=T9o0TY0OWdgi6ztc
