# Laporan Praktikum Minggu 1
Topik:  "Arsitektur Sistem Operasi dan Kernel"

---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan  
- **NIM**   : 250202985  
- **Kelas** : 1IKRB

---

## Tujuan
> Mahasiswa mampu menjelaskan fungsi utama sistem operasi dan peran kernel serta system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **arsitektur dasar sistem operasi**: bagaimana komponen OS bekerja, serta bagaimana interaksi antara user, aplikasi, kernel, dan hardware terjadi.  

Mahasiswa juga diperkenalkan pada:
- Perbedaan mode eksekusi **kernel mode** dan **user mode**.
- Mekanisme **system call** (panggilan sistem).
- Perbandingan model arsitektur OS seperti **monolithic kernel**, **layered approach**, dan **microkernel**.

Eksperimen akan dilakukan menggunakan perintah dasar Linux untuk melihat informasi kernel dan modul aktif.

---

## Langkah Praktikum
1. **Fork Repository**
   - Mahasiswa melakukan *fork* dari repositori utama `so-202501`.
   - Setiap mahasiswa wajib memiliki repositori individu pada akun GitHub masing-masing.

2. **Struktur Folder**
   - `docs/` → panduan & modul tiap pertemuan.
   - `praktikum/weekX-*` → artefak mingguan (kode, log, screenshot, laporan singkat).
   - `report/` → laporan bertumbuh (IMRaD) hingga final.
   - `scripts/`, `results/`, `vm/`, `docker/` → digunakan sesuai kebutuhan praktikum.

3. **Alur Pengerjaan**
   - Setiap minggu mahasiswa membaca panduan di `docs/`.
   - Melakukan praktik, menyimpan hasil di folder `praktikum/weekX-*`.
   - Menulis laporan singkat (`laporan.md`) di dalam folder minggu tersebut.
   - Menambahkan bukti (screenshot, log, konfigurasi) ke folder yang sesuai.

4. **Pengumpulan**
   - Setiap pertemuan, mahasiswa melakukan **commit & push** ke repositori masing-masing.
   - Dosen/Asisten akan melakukan pemeriksaan melalui GitHub.
   - Deadline pengumpulan: **maksimal W+2 setelah pertemuan praktikum**.
   - Keterlambatan akan dikenakan pengurangan nilai.
---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
whoami
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/sreenshot%20linux.png)

---

## Analisis
1.  Makna hasil percobaan.
      * uname -a, perintah ini digunakan untuk menampilkan semua informasi sistem yang mungkin yang dapat dicetak.
      * whoami, perintah ini digunakan untuk menampilkan nama pengguna (username) yang saat ini sedang masuk atau menjalankan perintah tersebut.
      * lsmod | head, perintah ini digunakan untuk menampilkan hanya baris-baris pertama dari daftar modul kernel yang sedang dimuat (loaded) di sistem Linux.
      * dmesg | head, perintah ini digunakan untuk menampilkan hanya baris-baris pertama dari log pesan buffer kernel.

2. Hubungan hasil dengan teori (fungsi kernel, system call, arsitektur OS).
   1. Fungsi Kernel dan Hasil Perintah
      Kernel adalah jantung dari Sistem Operasi, yang bertindak sebagai jembatan antara aplikasi pengguna (User Space) dan hardware.

      * uname -a membuktikan keberadaan dan identitas Kernel itu sendiri. Kernel inilah yang menentukan OS yang Anda jalankan.

      * lsmod menunjukkan fungsi Manajemen Modul Kernel, yang memungkinkan Kernel untuk beradaptasi dengan hardware baru tanpa harus dikompilasi ulang secara keseluruhan (monolithic kernel yang dimodifikasi).

      * dmesg memperlihatkan fungsi Manajemen Perangkat Keras dan Manajemen Booting Kernel. Semua pesan yang dicatat adalah aktivitas Kernel saat mendeteksi, menginisialisasi, dan menyiapkan hardware untuk digunakan.

   2. System Call (Panggilan Sistem)
      System Call adalah mekanisme yang digunakan aplikasi di User Space (tingkat keamanan rendah) untuk meminta layanan dari Kernel di Kernel Space (tingkat keamanan tinggi).

      * Perintah whoami harus menggunakan System Call (misalnya, geteuid()) untuk menanyakan identitas pengguna kepada Kernel, karena informasi keamanan ini hanya disimpan dan dikelola oleh Kernel. Ini adalah contoh klasik dari perlindungan Kernel: program tidak bisa langsung melihat siapa Anda; mereka harus meminta Kernel untuk memberi tahu.

   3. Arsitektur Sistem Operasi (User Space vs. Kernel Space)
      Arsitektur OS modern seperti Linux memisahkan ruang memori menjadi dua:

      * Kernel Space: Tempat Kernel berjalan. Memiliki akses penuh dan privileged ke hardware.

      * User Space: Tempat aplikasi dan shell berjalan. Hanya dapat mengakses hardware melalui System Call.

      * Semua perintah (uname, whoami, lsmod, dmesg) dijalankan di User Space (oleh shell), tetapi untuk  mendapatkan informasi yang mereka tampilkan, mereka HARUS berinteraksi dengan Kernel Space.

      * Misalnya, lsmod (User Space) membaca data dari struktur data internal Kernel (/proc/modules yang dihasilkan Kernel Space). Interaksi ini menunjukkan bagaimana User Space meminta informasi yang dikelola oleh Kernel Space.




---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.
1. Kernel Adalah Pusat Kontrol: Perintah seperti uname -a dan dmesg menunjukkan bahwa Kernel adalah inti yang mengelola hardware dan fungsi dasar OS; lsmod menunjukkan Kernel dapat diperluas.

2. Pemegang Akses Terpisah: OS membagi operasi menjadi mode aman (Kernel Mode) dan terbatas (User Mode). Program di User Mode (seperti whoami) harus menggunakan System Call untuk meminta layanan dari Kernel, menjaga sistem tetap stabil.

3. Shell = Antarmuka Status: Perintah dasar shell berfungsi sebagai alat langsung untuk melihat dan memverifikasi data operasional internal yang dikendalikan oleh Kernel.

---

## Quiz
1. Sebutkan tiga fungsi utama sistem operasi. 
   **Jawaban:**
   
   **Manajemen Sumber Daya, Antarmuka Pengguna, dan Manajemen Berkas.**  
2. Jelaskan perbedaan antara *kernel mode* dan *user mode*.    
   **Jawaban:**
   
   **Perbedaan utama antara Kernel Mode dan User Mode terletak pada tingkat hak akses dan proteksi yang diberikan kepada kode yang sedang dieksekusi oleh CPU. Ini adalah konsep fundamental dalam arsitektur sistem operasi modern (seperti Linux, Windows, macOS) untuk memastikan stabilitas dan keamanan sistem.**  
3. Sebutkan contoh OS dengan arsitektur monolithic dan microkernel.  
   **Jawaban:**

* **Monolihic: Linux Kernel, FreeBSD, Solaris (Oracle Solaris), dan Windows NT Kernel**.
* **Microkernel:MINIX, QNX, L4, dan Mach.**
 

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?
**Belajar dari nol karena baru pertama kali memegang laptop saat malam Kamis, belajar cara mengoperasikan laptop, mengoperasikan Vs Code, Git Bash, Draw.io, Github, sempat sertess karena saat commit tugas error, lalu saat berhasil commit, ternyata hasil commitannya kosong karena belum di save, mengerjakan laporan sampai subuh.**  
- Bagaimana cara Anda mengatasinya? 
**Saya belajar dari mas Prastian Hidayat sampai subuh.** 

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_