Dalam dunia pemrograman, ada banyak cara buat mengurutkan data, dan salah satu yang paling dasar itu namanya Bubble Sort. Bayangin aja kayak gelembung sabun di dalam air; yang paling ringan bakal pelan-pelan naik ke atas, sedangkan yang berat bakal tetap di bawah. Di dalam kode ini, "berat" atau "ringannya" itu diukur dari seberapa banyak barang yang dibawa sama pelanggan di sebuah antrean.

Jadi, kegunaan utama dari kode ini adalah buat bikin sistem antrean jadi lebih teratur dan efisien. Fokusnya bukan cuma sekadar urut angka, tapi lebih ke manajemen prioritas. Kalau biasanya antrean itu sistemnya siapa cepat dia dapat (FIFO), kode ini mengubah aturannya jadi "siapa yang urusannya paling dikit, dia yang maju duluan."

Cara kerjanya simpel tapi telaten. Program bakal ngecek barisan pelanggan dari paling depan. Kalau ada orang yang bawa barang lebih banyak dibanding orang tepat di belakangnya, posisi mereka langsung ditukar. Hal ini dilakuin terus-menerus sampai nggak ada lagi posisi yang perlu ditukar.

Hasil akhirnya, pelanggan yang cuma bawa satu atau dua barang—kayak si Dewi atau Budi—bakal otomatis kegeser ke depan. Sementara yang bawaannya seabrek kayak si Andi bakal pelan-pelan pindah ke posisi paling belakang. Ini ngebantu banget biar antrean nggak macet total cuma gara-gara satu orang yang belanjaannya satu troli penuh, jadi pelayanan pun terasa lebih cepat buat banyak orang.

Penjelasan Alur Input & output:
<img width="1919" height="1079" alt="Screenshot 2026-04-27 201842" src="https://github.com/user-attachments/assets/e299b4aa-755a-4901-aaf2-b85d9f81f407" />
<img width="1915" height="1065" alt="Screenshot 2026-04-27 201937" src="https://github.com/user-attachments/assets/5d4eaa11-ac06-45ef-b298-8c0c53e0e8ea" />
Pengurutan data itu sebenarnya hal yang lumrah di dunia pemrograman, dan salah satu metode dasar yang sering digunakan adalah Bubble Sort. Konsepnya sederhana, mirip seperti gelembung udara yang naik ke permukaan air; data yang nilainya lebih kecil bakal pelan-pelan "naik" ke posisi depan, sementara yang nilainya besar bakal "tenggelam" ke posisi belakang.

Kalau melihat alur dari kode tersebut, semuanya bermula dari input berupa daftar nama pelanggan beserta jumlah barang bawaannya. Data ini awalnya masih acak, di mana Andi yang bawa 15 barang ada di urutan pertama, padahal ada Dewi yang cuma bawa 1 barang tapi posisinya terselip di tengah. Kondisi input yang tidak teratur ini bikin antrean jadi kurang efisien kalau ingin menerapkan sistem prioritas.

Setelah data masuk, proses di dalam kode mulai bekerja dengan membandingkan pelanggan yang berdiri bersebelahan. Jadi, sistem bakal mengecek pelanggan pertama dan kedua; kalau pelanggan pertama membawa barang lebih banyak, posisinya langsung ditukar. Langkah ini terus diulang ke pelanggan berikutnya sampai ke ujung antrean. Karena ada pengecekan berulang, pelanggan yang bawa barang sedikit otomatis bakal bergeser ke barisan depan, dan yang bawaannya banyak bakal pindah ke posisi belakang.

Hasil akhir atau output dari proses ini adalah daftar pelanggan yang sudah rapi berdasarkan jumlah barangnya. Urutannya bakal berubah total dari yang tadinya acak menjadi Dewi (1 barang), Budi (3 barang), Eko (7 barang), Citra (10 barang), dan terakhir Andi (15 barang). Dengan begitu, tujuan utama kode tercapai, yaitu mengubah antrean yang berantakan jadi sistem yang lebih teratur sesuai prioritas jumlah belanjaan.

Link Youtube: https://youtu.be/UwwGwYsaXVg?si=Qcmgeuf8cGoWvquU
