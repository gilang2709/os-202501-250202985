
# Laporan Praktikum Minggu 7
Topik: Sinkronisasi Proses dan Masalah Deadlock  

---

### Identitas Kelompok
| Nama | NIM |
| :--- | :--- |
| M. Habibi Nur Ramadhan | 250202949 |
| Fatkhurrohman Gilang Ramadhan | 250202985 |
| Farhan Ramdhani | 250202938 |
| Yusuf Anwar | 250202971 |

**Kelas 1IKRB**

---

## Pendahuluan
Tujuan praktikum ini adalah untuk:
1. Mengidentifikasi empat kondisi penyebab deadlock (*mutual exclusion, hold and wait, no preemption, circular wait*).  
2. Menjelaskan mekanisme sinkronisasi menggunakan *semaphore* atau *monitor*.  
3. Menganalisis dan memberikan solusi untuk kasus deadlock.  
4. Berkolaborasi dalam tim untuk menyusun laporan analisis.  
5. Menyajikan hasil studi kasus secara sistematis.  

---

## Metode

Metode yang digunakan adalah simulasi berbasis studi kasus **Dining Philosophers** dengan langkah-langkah sebagai berikut:

1.  **Eksperimen 1 (Versi Deadlock):** Implementasi skenario dasar di mana setiap Philosopher (*proses*) mengambil garpu kiri, kemudian garpu kanan. Simulasi dijalankan untuk mengamati dan mengidentifikasi kondisi deadlock.
2.  **Eksperimen 2 (Versi Fixed):** Memodifikasi skenario dengan menambahkan mekanisme **sinkronisasi** menggunakan **semaphore** untuk membatasi jumlah Philosopher yang dapat berada di "ruang makan" (*Critical Section*) secara bersamaan. Solusi yang dipilih adalah **membatasi maksimal $N-1$ Philosopher** (4 dari 5) yang dapat mengambil garpu.
3.  **Eksperimen 3 (Analisis):** Menganalisis bagaimana solusi semaphore pada Eksperimen 2 berhasil mencegah deadlock dengan memutus salah satu dari empat kondisi penyebabnya.
  
---


### Dasar Teori

1. Deadlock

Deadlock adalah kondisi ketika beberapa proses saling menunggu satu sama lain sehingga tidak ada satu pun yang bisa melanjutkan.
Deadlock terjadi jika empat kondisi berikut muncul secara bersamaan:
   1. Mutual Exclusion
Resource hanya bisa dipakai satu proses pada satu waktu.
   2. Hold and Wait
Proses sudah memegang satu resource dan menunggu resource lain.
   3. No Preemption
Resource tidak bisa direbut paksa dari proses yang sedang menggunakannya.
   4. Circular Wait
Terdapat proses yang saling menunggu secara melingkar.

Jika salah satu dari kondisi ini dihilangkan, deadlock tidak terjadi.

2. Critical Section

Critical section adalah bagian kode di mana proses mengakses data bersama (shared data).
Jika dua proses masuk critical section bersamaan, data bisa rusak atau hasil perhitungan jadi salah.
Karena itu, diperlukan mekanisme untuk memastikan bahwa hanya satu proses yang boleh masuk critical section pada waktu tertentu.

3. Sinkronisasi Proses

Sinkronisasi adalah cara untuk mengatur proses atau thread agar tidak saling bertabrakan ketika mengakses resource yang sama.
Tujuan sinkronisasi:

* mencegah race condition,
* menjaga konsistensi data,
* mengatur urutan eksekusi,
* menghindari deadlock dan starvation.

Tanpa sinkronisasi, program paralel dapat menghasilkan output yang salah atau macet.

4. Semaphore

Semaphore adalah mekanisme sinkronisasi berbasis counter yang digunakan untuk mengatur akses ke resource.
Terdiri dari dua operasi utama :

wait() → mengurangi nilai semaphore dan bisa membuat proses menunggu,
signal() → menambah nilai semaphore dan membangunkan proses lain.

Semaphore sering digunakan untuk:

* mengatur mutual exclusion,
* membatasi jumlah proses yang boleh masuk ke suatu area,
* mengatur giliran proses.

5. Monitor

Monitor adalah mekanisme sinkronisasi tingkat tinggi yang lebih aman daripada semaphore.
Ciri-cirinya:

* hanya satu proses yang bisa masuk ke dalam monitor pada satu waktu,
* punya prosedur/fungsi yang aman untuk mengakses data bersama,
* punya condition variable (wait / notify) untuk mengatur antrian proses.

Monitor mempermudah sinkronisasi karena aturan mutual exclusion sudah otomatis.

6. Masalah "Dining Philosophers"

Dining Philosophers adalah masalah klasik dalam sistem operasi yang menggambarkan lima philosopher yang duduk melingkar, masing-masing membutuhkan dua garpu untuk makan. Garpu diletakkan di antara setiap dua philosopher.

Masalah ini menggambarkan:
* bagaimana proses saling berbagi resource,
* bagaimana deadlock bisa terjadi,
* bagaimana sinkronisasi dilakukan supaya semua proses tetap berjalan.

Pada versi sederhana, deadlock dapat terjadi ketika semua philosopher mengambil satu garpu dan menunggu garpu berikutnya.

Solusi umum untuk menghilangkan deadlock :

* membatasi jumlah philosopher yang boleh mengambil garpu,
* mengubah urutan pengambilan garpu (misalnya ganjil/ genap),
* menambahkan “waiter” (monitor) yang mengatur giliran philosopher makan.

---

### Langkah Praktikum
1. **Persiapan Tim**
   - Bentuk kelompok beranggotakan 3–4 orang.  
   - Tentukan ketua dan pembagian tugas (analisis, implementasi, dokumentasi).

2. **Eksperimen 1 – Simulasi Dining Philosophers (Deadlock Version)**
   - Implementasikan versi sederhana dari masalah *Dining Philosophers* tanpa mekanisme pencegahan deadlock.  
   - Contoh pseudocode:
     ```text
     while true:
       think()
       pick_left_fork()
       pick_right_fork()
       eat()
       put_left_fork()
       put_right_fork()
     ```
   - Jalankan simulasi atau analisis alur (boleh menggunakan pseudocode atau diagram alur).  
   - Identifikasi kapan dan mengapa deadlock terjadi.

3. **Eksperimen 2 – Versi Fixed (Menggunakan Semaphore / Monitor)**
   - Modifikasi pseudocode agar deadlock tidak terjadi, misalnya:
     - Menggunakan *semaphore (mutex)* untuk mengontrol akses.
     - Membatasi jumlah filosof yang dapat makan bersamaan (max 4).  
     - Mengatur urutan pengambilan garpu (misal, filosof terakhir mengambil secara terbalik).  
   - Analisis hasil modifikasi dan buktikan bahwa deadlock telah dihindari.

4. **Eksperimen 3 – Analisis Deadlock**
   - Jelaskan empat kondisi deadlock dari versi pertama dan bagaimana kondisi tersebut dipecahkan pada versi fixed.  
   - Sajikan hasil analisis dalam tabel seperti contoh berikut:

     | Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
     |------------------|---------------------------|------------------------|
     | Mutual Exclusion | Ya (satu garpu hanya satu proses) | Gunakan semaphore untuk kontrol akses |
     | Hold and Wait | Ya | Hindari proses menahan lebih dari satu sumber daya |
     | No Preemption | Ya | Tidak ada mekanisme pelepasan paksa |
     | Circular Wait | Ya | Ubah urutan pengambilan sumber daya |

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua diagram, screenshot simulasi, dan hasil diskusi di:
     ```
     praktikum/week7-concurrency-deadlock/screenshots/
     ```
   - Tuliskan laporan kelompok di `laporan.md` (format IMRaD singkat: *Pendahuluan, Metode, Hasil, Analisis, Diskusi*).

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 7 - Sinkronisasi Proses & Deadlock"
   git push origin main
   ```


---

## Hasil

### Hasil Eksperimen
| Eksperimen | Skenario | Hasil Kunci | Catatan |
| :--- | :--- | :--- | :--- |
| **Eksperimen 1** | Tanpa Sinkronisasi | Terjadi **Deadlock** | Semua Philosopher mengambil garpu kiri, lalu menunggu garpu kanan. Terjadi *Circular Wait* dan semua proses macet. |
| **Eksperimen 2** | Dengan Semaphore (N-1) | **Deadlock Terhindari** | Proses makan-dan-berpikir berjalan lancar. Tidak ada proses yang terblokir secara permanen. |

> **Eksperimen 1 - Versi Deadlock:**
> ![Screenshot hasil](./screenshots/Eksperimen%201.jpeg)
> **Eksperimen 2 - Versi Fixed:**
> ![Screenshot hasil](./screenshots/Eksperimen%202.jpeg)

---
## Analisis
### Eksperimen 1

![Screenshot hasil](./screenshots/Eksperimen%201.jpeg)

Deadlock terjadi ketika setiap philosopher mengambil garpu kiri (lock berhasil) lalu menunggu garpu kanan yang sedang dipegang tetangga. Kondisi empat syarat deadlock terpenuhi: mutual exclusion (garpu eksklusif), hold-and-wait (pegang 1 garpu sambil menunggu 1 lagi), no preemption (tidak bisa dipaksa melepaskan garpu), circular wait (lingkaran tunggu antara philosophers).

---

### Eksperimen 2

![Screenshot hasil](./screenshots/Eksperimen%202.jpeg)
1. Analisis Semaphore (Membatasi Akses Ruang Makan)Pencegahan Kondisi: Mencegah Circular Wait.
2. Bukti: Dengan membatasi hanya N-1 filosof yang dapat mencoba mengambil garpu pada saat yang sama, Anda memastikan bahwa setidaknya satu filosof akan selalu dapat mengambil garpu kedua.
   * Jika N=5, dan 4 filosof (P0, P1, P2, P3) berhasil masuk ruang makan dan masing-masing mengambil garpu kiri mereka (F0, F1, F2, F3), maka garpu F4 dan F5 (atau F0) masih tersedia.
   * Salah satu dari 4 filosof ini, misalnya P3, akan mencoba mengambil F4. 
   * Jika P3 berhasil, ia dapat makan dan melepaskan F3 dan F4.
   * Begitu P3 keluar dan melepaskan semaphore, filosof P4 dapat masuk.
   * Karena selalu ada jatah garpu yang tersisa, siklus tunggu yang melingkar (Circular Wait) tidak dapat terbentuk secara permanen.
---

### Eksperimen 3

| Kondisi Deadlock | Terjadi di Versi Deadlock | Solusi di Versi Fixed |
|---------|------|-----------|
| 1. Mutual Exclusion | Ya. Satu garpu (Lock) hanya dapat dipegang oleh satu filosof (proses). | Dipertahankan. Tidak bisa dipecahkan karena sifat fisik garpu. Solusi fokus pada kondisi lain. |
| 2. Hold and Wait | Ya. Filosof memegang garpu kiri sambil menunggu garpu kanan. | Diredam. Solusi N-1 memastikan penantian ini tidak berujung pada siklus tak terbatas. (Pada strategi lain, filosof mungkin diharuskan mengambil keduanya sekaligus). |
| 3. No Preemption | Ya. Garpu tidak dapat direbut paksa dari filosof yang memegangnya (hanya dilepas secara sukarela). | Dipertahankan. Tidak ada mekanisme pelepasan paksa yang digunakan dalam solusi ini. |
| 4. Circular Wait | Ya. Filosof menunggu garpu tetangga, membentuk rantai melingkar. | Dipecahkan. Gunakan Semaphore (N-1) untuk membatasi jumlah filosof di meja, mencegah rantai melingkar terbentuk. (Ini adalah cara memecah urutan pengambilan sumber daya secara kolektif). |

---

## Kesimpulan
1. Praktikum ini berhasil mendemonstrasikan empat kondisi penyebab deadlock dalam masalah Dining Philosophers, yaitu mutual exclusion, hold and wait, no preemption, dan circular wait, serta bagaimana kondisi tersebut dapat diidentifikasi dan dianalisis melalui simulasi.
2. Penggunaan semaphore sebagai mekanisme sinkronisasi terbukti efektif untuk mencegah deadlock, khususnya dengan membatasi jumlah filosof yang dapat mengakses sumber daya secara bersamaan, sehingga memutus siklus tunggu melingkar.
3. Kolaborasi tim dalam analisis, implementasi, dan dokumentasi memperkuat pemahaman konsep sinkronisasi proses, serta menekankan pentingnya solusi pencegahan deadlock dalam desain sistem operasi untuk menghindari stagnasi proses.

---

## Diskusi
### Quiz
1. Sebutkan empat kondisi utama penyebab deadlock.  
   **Jawaban:**  
   - *Mutual Exclusion*: Setiap sumber daya hanya dapat digunakan oleh satu proses pada satu waktu.  
   - *Hold and Wait*: Proses menahan satu sumber daya sambil menunggu sumber daya lain yang dipegang oleh proses lain.  
   - *No Preemption*: Sumber daya tidak dapat direbut paksa dari proses yang memegangnya; hanya dapat dilepas secara sukarela.  
   - *Circular Wait*: Terbentuknya siklus tunggu di mana setiap proses menunggu sumber daya yang dipegang oleh proses berikutnya dalam rantai.

2. Mengapa sinkronisasi diperlukan dalam sistem operasi?  
   **Jawaban:**  
   - Mencegah Kondisi Balapan: Memastikan proses tidak mengakses data bersama pada saat yang sama, menghindari hasil yang tidak konsisten.
   - Pengecualian Bersama: Hanya mengizinkan satu proses di bagian kritis pada satu waktu.
   - Koordinasi Proses: Memungkinkan proses menunggu kondisi tertentu (misalnya, produsen-konsumen).
   - Pencegahan Kebuntuan: Menghindari penantian melingkar dan pemblokiran tak terbatas dengan menggunakan penanganan sumber daya yang tepat.
   - Komunikasi Aman: Memastikan data/pesan antar proses dikirim, diterima, dan diproses secara berurutan.
   - Keadilan: Mencegah kelaparan dengan memberikan semua proses akses yang adil terhadap sumber daya.

3. Jelaskan perbedaan antara semaphore dan monitor.  
   **Jawaban:**  
   - Semaphore adalah variabel penghitung primitif (tingkat rendah) yang digunakan untuk sinkronisasi. Ia hanya memiliki dua operasi atomik (wait() dan signal()). Karena fleksibel, programmer harus sangat berhati-hati menggunakannya; lupa memanggil signal dapat menyebabkan deadlock.
   - Monitor adalah struktur bahasa tingkat tinggi (tingkat atas) yang menggabungkan data bersama dan prosedur yang mengoperasikannya. Keunggulannya adalah ia secara otomatis menjamin mutual exclusion (hanya satu proses yang aktif di dalamnya). Hal ini menjadikannya lebih aman dan kurang rawan kesalahan dibandingkan semaphore.
  
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini? 
- Pertamakali kerja kelompok harus beradaptasi dengan teman, karena biasanya mengerjakan sendiri. 
- Bagaimana cara Anda mengatasinya?  
- Belajar berdiskusi bersama teman.

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
