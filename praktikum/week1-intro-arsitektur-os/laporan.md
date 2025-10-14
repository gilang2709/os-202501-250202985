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
1. **Setup Environment**
   - Pastikan Linux (Ubuntu/WSL) sudah terinstal.
   - Pastikan Git sudah dikonfigurasi dengan benar:
     ```bash
     git config --global user.name "Nama Anda"
     git config --global user.email "email@contoh.com"
     ```

2. **Diskusi Konsep**
   - Baca materi pengantar tentang komponen OS.
   - Identifikasi komponen yang ada pada Linux/Windows/Android.

3. **Eksperimen Dasar**
   Jalankan perintah berikut di terminal:
   ```bash
   uname -a
   whoami
   lsmod | head
   dmesg | head
   ```
   Catat dan analisis modul kernel yang tampil.

4. **Membuat Diagram Arsitektur**
   - Buat diagram hubungan antara *User → System Call → Kernel → Hardware.*
   - Gunakan **draw.io** atau **Mermaid**.
   - Simpan hasilnya di:
     ```
     praktikum/week1-intro-arsitektur-os/screenshots/diagram-os.png
     ```

5. **Penulisan Laporan**
   - Tuliskan hasil pengamatan, analisis, dan kesimpulan ke dalam `laporan.md`.
   - Tambahkan screenshot hasil terminal ke folder `screenshots/`.

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 1 - Arsitektur Sistem Operasi dan Kernel"
   git push origin main
   ```

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
![Screenshot hasil](./screenshots/screenshots%20linux%20minggu%201.png)

---

## Analisis 1
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

3. Apa perbedaan hasil di lingkungan Os berbeda(Linux vs Windows)
   * Linux fokus pada kesederhanaan dan konsistensi menggunakan nomor , sementara Windows fokus pada kontrol dan struktur menggunakan tiket objek kompleks.


## Analisis 2

### Perbedaan Antara Monolithic Kernel, Microkernel, dan Layered Arsitechture

#### 1. Monolithic Kernel
Monolithic Kernel adalah desain arsitektur sistem operasi (OS) di mana semua elemen inti, seperti driver perangkat, memori, pengelolaan proses, dan sistem file, terintegrasi menjadi satu blok tunggal. Ini beroperasi di level kernel dan memiliki akses langsung ke hardware.

##### Kelebihan
Kelebihan utama desain ini adalah kecepatan eksekusinya yang tinggi. Semua komponen berkomunikasi secara langsung tanpa lapisan tambahan, yang membuat sistem operasi sangat responsif untuk beban kerja berat seperti server web atau permainan.  Selain itu, ia menghemat lebih banyak sumber daya, termasuk memori dan CPU, dan pengembangannya lebih mudah karena kode yang saling terkait memungkinkan penambahan fitur atau dukungan hardware baru tanpa mengalami kesulitan yang berlebihan.

##### Kekurangan
Kekurangan utamanya terletak pada keamanan yang rentan. Kurangnya isolasi yang kuat membuat kesalahan kecil di modul mana pun dapat menghancurkan seluruh sistem.  Akibat ukuran kode yang besar dan ketergantungan antar-komponen, pemeliharaan menjadi lebih sulit, yang membuat debugging memakan waktu lama dan mengandung risiko perubahan yang tinggi.  Akses penuh ke hardware meningkatkan kerentanan terhadap serangan, membuatnya tidak cocok untuk lingkungan yang membutuhkan kestabilan atau modularitas tinggi.

Contoh OS: Linux Kernel, FreeBSD, Solaris (Oracle Solaris), dan Windows NT Kernel adalah beberapa contoh utama.

#### 2. Microkernel
Microkernel menggunakan pendekatan minimalis untuk arsitektur sistem operasi, di mana kernel menangani tugas-tugas dasar seperti komunikasi antar-proses dan pengelolaan ruang alamat. Layanan lain, seperti driver dan sistem file, berjalan sebagai proses terpisah di ruang pengguna.

##### Kelebihhan
Kelebihan utama microkernel adalah tingkat keamanan dan keandalan yang lebih tinggi berkat isolasi ketat antar-modul. Kegagalan di satu modul, misalnya driver, tidak akan merusak sistem secara keseluruhan, menjadikannya pilihan yang sangat baik untuk aplikasi penting dalam bidang medis, mobil, atau keamanan siber.  Selain itu, modularitasnya yang kuat memudahkan pengembangan, pengujian, dan pembaruan independen tanpa perlu menghidupkan kembali sistem operasi, yang membuat pemeliharaan lebih fleksibel dan efisien.  Desain sederhana ini meningkatkan portabilitas ke berbagai hardware dan memungkinkan verifikasi formal untuk keamanan tambahan, yang sangat bermanfaat untuk sistem real-time atau riset.

##### Kekurangan
Di antara kelebihannya, microkernel juga mempunyai kekurangan. Microkernel seringkali mengalami penurunan performa karena overhead dari mekanisme IPC seperti pengiriman pesan yang menambah latensi dan meningkatkan penggunaan CPU dan memori. Ini tidak cocok untuk tugas berat seperti pemrosesan data real-time di server atau grafis berat.  Pengembangan juga lebih kompleks karena memerlukan desain IPC dan integrasi modul terpisah, yang dapat memperlambat proses awal dan meningkatkan biaya.  Selain itu, karena proses terpisah, ukuran sistem keseluruhan cenderung meningkat, dan adopsinya masih terbatas pada penggunaan sehari-hari seperti desktop atau server umum, di mana monolithic kernel seringkali lebih baik dari segi kinerja.

Contoh OS: MINIX, QNX, L4, dan Mach.

#### 3. Layered Architechture
Layered architechture membagi komponen sistem operasi menjadi lapisan hierarkis. Ini berarti bahwa setiap lapisan menggunakan dukungan dari lapisan bawah untuk menyediakan layanan abstrak ke lapisan di atasnya. Ini termasuk hardware di dasar, kernel, driver, dan antarmuka pengguna, misalnya.  Metode ini, seperti model OSI jaringan, menekankan modularitas dan pemisahan tugas.

##### kelebihan
Layered architechture memiliki keunggulan dalam modularitas karena membagi fungsi menjadi lapisan terpisah, yang memungkinkan pengembangan dan pengujian independen. Perubahan di satu lapisan jarang memengaruhi yang lain, sehingga debugging dan pemeliharaan menjadi lebih mudah.  Selain itu, desain hierarkis mendukung portabilitas yang baik. Lapisan atas dapat disesuaikan dengan hardware baru tanpa menyentuh lapisan bawah dan mendorong standarisasi layanan, yang membuat sistem lebih mudah dipahami dan dikembangkan oleh tim besar, terutama untuk proyek sistem operasi yang kompleks dengan banyak pengguna.

##### Kekurangan
Meskipun modular, arsitektur lapisan sering menyebabkan overhead performa karena interaksi antar-lapisan memerlukan pengiriman data melalui seluruh hirarki. Ini meningkatkan latensi dan mengkonsumsi sumber daya, dan tidak efisien untuk aplikasi real-time atau akses hardware langsung.  Selain itu, ketergantungan antar-lapisan dapat menimbulkan risiko, perubahan desain tidak mudah dilakukan tanpa mengganggu struktur keseluruhan, yang menghambat inovasi dan membuatnya kurang fleksibel daripada monolithic atau microkernel.

Contoh OS: THE OS (1960-an, karya Edsger Dijkstra), Multics (1960-an, pendahulu Unix), Windows NT (dasar sistem Windows modern), Model OSI (1984, dari ISO), dan Model TCP/IP (dasar internet).

#### 4. Analisis: Model Arsitektur Paling Relevan Saat Ini
 Di era cloud, IoT, dan AI, arsitektur hybrid jadi pilihan terbaik untuk sistem operasi (OS). Ini seperti campuran dari monolithic kernel yang cepat, aman seperti microkernel, dan mudah diatur seperti layered architecture. Contohnya Linux, yang dipakai di 96% server dunia, pakai Kubernetes agar pekerjaan yang berat berjalan lancar tanpa sering error atau mati.

TCP/IP tetap menjadi dasar untuk arsitektur jaringan, dengan empat lapisan yang lebih efisien daripada model OSI, menangani 99% lalu lintas internet melalui penyetaraan rute IP dan keandalan TCP/UDP. Ekstensi seperti QUIC mengurangi latensi pada jaringan 5G, dan IPv6 dan TLS meningkatkan keamanan berbasis zero-trust untuk komputasi tepi.

Intinya, hybrid architecture untuk OS dan TCP/IP untuk jaringan adalah model paling relevan untuk sistem modern, karena menyeimbangkan efisiensi dengan keandalan di lingkungan dinamis seperti cloud dan IoT.

---

#### Kesimpulan
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