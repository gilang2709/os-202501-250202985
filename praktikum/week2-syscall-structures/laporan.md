
# Laporan Praktikum Minggu 2
Struktur System Call dan Fungsi Kernel


---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan  
- **NIM**   : 250202985 
- **Kelas** : 1IKRB

---

## Tujuan 
>Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menjelaskan konsep dan fungsi system call dalam sistem operasi.
2. Mengidentifikasi jenis-jenis system call dan fungsinya.
3. Mengamati alur perpindahan mode user ke kernel saat system call terjadi.
4. Menggunakan perintah Linux untuk menampilkan dan menganalisis system call.

---

## Dasar Teori
Pada praktikum minggu ini, mahasiswa akan mempelajari **mekanisme system call dan struktur sistem operasi**.  
System call adalah antarmuka antara program aplikasi dan kernel yang memungkinkan aplikasi berinteraksi dengan perangkat keras secara aman melalui layanan OS.

Mahasiswa akan melakukan eksplorasi terhadap:
- Jenis-jenis system call yang umum digunakan (file, process, device, communication).
- Alur eksekusi system call dari mode user menuju mode kernel.
- Cara melihat daftar system call yang aktif di sistem Linux.

---

## Langkah Praktikum
1. **Setup Environment**
   - Gunakan Linux (Ubuntu/WSL).
   - Pastikan perintah `strace` dan `man` sudah terinstal.
   - Konfigurasikan Git (jika belum dilakukan di minggu sebelumnya).

2. **Eksperimen 1 – Analisis System Call**
   Jalankan perintah berikut:
   ```bash
   strace ls
   ```
   > Catat 5–10 system call pertama yang muncul dan jelaskan fungsinya.  
   Simpan hasil analisis ke `results/syscall_ls.txt`.

3. **Eksperimen 2 – Menelusuri System Call File I/O**
   Jalankan:
   ```bash
   strace -e trace=open,read,write,close cat /etc/passwd
   ```
   > Analisis bagaimana file dibuka, dibaca, dan ditutup oleh kernel.

4. **Eksperimen 3 – Mode User vs Kernel**
   Jalankan:
   ```bash
   dmesg | tail -n 10
   ```
   > Amati log kernel yang muncul. Apa bedanya output ini dengan output dari program biasa?

5. **Diagram Alur System Call**
   - Buat diagram yang menggambarkan alur eksekusi system call dari program user hingga kernel dan kembali lagi ke user mode.
   - Gunakan draw.io / mermaid.
   - Simpan di:
     ```
     praktikum/week2-syscall-structure/screenshots/syscall-diagram.png
     ```

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 2 - Struktur System Call dan Kernel Interaction"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
strace ls
strace -e trace=open,read,write,close cat /etc/passwd
dmesg | tail -n 10
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/strace%20ls.png)
![Screenshot hasil](./screenshots/strace%20-e%20trace=open,read,write,close%20cat%20etcpasswd.png)
![Screenshot hasil](./screenshots/dmesg%20%20tail%20-n%2010.png)

## Eksperimen 1 – Analisis System Call
| No  | Perintah/System Call | Fungsi                           | Output Contoh                         | Tujuan                                                                                      |
|------|---------------------|---------------------------------|-------------------------------------|----------------------------------------------------------------------------------------------|
| 1    | execve         | Menjalankan Program Baru        | `execve	"/bin/ls", ["ls"]`, | Mengganti proses saat ini dengan program baru.                                                          |
| 2    | brk              | Mengubah Ukuran Data Segment         | `brk	NULL, kemudian 0x7d827feaa000` | Digunakan untuk mengubah ukuran data segment program.                              |
| 3    | access          | Memeriksa Izin Akses | `access	"/etc/ld.so.preload", R_OK` | Memeriksa apakah process memiliki izin untuk mengakses file atau direktori tertentu.                                         |
| 4    | openat               | Membuka File atau Direktori       | `openat	`AT_FDCWD, "/etc/ld.so.cache", O_RDONLY` | Membuat file descriptor baru yang merujuk ke file atau direktori yang ditentukan oleh jalur (pathname).                                                     |
| 5    | mmap          | Memetakan File ke Memori                | `mmap	NULL, 35463, PROT_READ, MAP_PRIVATE, 3, 0)`                     | Memetakan file atau perangkat ke ruang alamat memori proses.                                        |
| 6    | fstat         | Mendapatkan Status File  | `fstat	`3, {st_mode=S_IFREG` | Mendapatkan informasi status untuk file yang baru dibuka (pustaka liblinux-so.1).  |
| 7    | read         | Membaca Data dari File | `read	3, "\177ELF\2\1\1\0\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\220\0\4\0\0\0\0\0"..., 832` | Membaca data sejumlah byte tertentu dari file yang terkait dengan file descriptor yang diberikan (3) ke dalam buffer.         |

## Eksperimen 2 – Menelusuri System Call File I/O

   * Proses dimulai saat program cat meminta kernel untuk membuka file /etc/passwd. Kernel merespons dengan mengalokasikan dan mengembalikan file descriptor (FD) 3. FD ini adalah kunci unik yang akan digunakan cat untuk merujuk pada file tersebut selama operasi I/O. Tahap ini krusial karena menyiapkan jalur komunikasi antara aplikasi dan sumber daya file di sistem operasi.

   * Selanjutnya, program menggunakan system call read untuk memindahkan data. Awalnya, read mungkin memuat pustaka yang dibutuhkan, tetapi panggilan utama (read(3, ..., 1443)) meminta kernel untuk menyalin seluruh konten file (1443 bytes) dari disk ke dalam buffer di memori proses cat. Kernel bertindak sebagai driver yang mengelola transfer data yang efisien dan aman.

   * Setelah data berada di memori, cat memanggil system call write untuk menampilkan konten tersebut. Perintah write(1, ..., 1443) menginstruksikan kernel untuk mengambil data 1443 bytes dari buffer program dan menuliskannya ke File Descriptor 1 (Standard Output), yaitu terminal. Kernel bertugas mengirimkan data ini ke perangkat output yang sesuai, sehingga pengguna dapat melihat isi dari /etc/passwd.

   * Terakhir, setelah semua I/O selesai, program memanggil system call close(3). Perintah ini memerintahkan kernel untuk menutup koneksi dan melepaskan file descriptor 3. Kernel membebaskan nomor FD tersebut dari alokasi, memastikan bahwa tidak ada sumber daya yang terbuang dan nomor tersebut siap digunakan kembali oleh proses atau file lain.

## Eksperimen 3 – Mode User vs Kernel
   * Perbedaan mendasar antara log kernel (strace) dan output program biasa adalah pada fokus dan tujuannya. Log kernel adalah catatan teknis tingkat rendah mengenai proses internal, yaitu perintah (read, write) yang dikeluarkan program ke kernel untuk meminta layanan. Sebaliknya, output program biasa adalah hasil akhir tingkat tinggi yang disajikan kepada pengguna, yaitu data mentah dari file tersebut. Singkatnya, strace menampilkan bagaimana program bekerja, sedangkan output biasa menampilkan apa yang berhasil dilakukan program.

---

## Analisis
- Hasil percobaan.  
  * strace ls tujuannya adalah untuk melacak (trace) semua system call dan sinyal yang dibuat dan diterima oleh perintah ls saat dieksekusi.
  * strace berfungsi sebagai "detektif" yang mengintip setiap interaksi antara program (ls) dengan kernel Linux (inti sistem operasi).
  
  * strace -e trace=open,read,write,close cat /etc/passwd berfungsi untuk menampilkan dan membatasi (memfilter) system call yang dipantau ketika perintah cat /etc/passwd dijalankan.
  * Tujuannya adalah untuk melihat secara detail hanya langkah-langkah dasar interaksi file (open, read, write, close) yang dilakukan oleh program cat saat mencoba membaca dan menampilkan isi file /etc/passwd.

  * dmesg | tail -n 10 berfungsi untuk menampilkan sepuluh baris terakhir dari log kernel sistem (Kernel Ring Buffer).
  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS). 
  * strace menampilkan aktivitas di User Mode saat program meminta layanan.

  * dmesg menampilkan hasil kerja dan status di Kernel Mode yang merupakan respons dari aktivitas tersebut.  

- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  
  * Perbedaan (Linux vs Windows) tidak terletak pada hasil fungsionalnya, melainkan pada mekanisme internal, bahasa pemrograman sistem, dan objek yang digunakan untuk merepresentasikan sumber daya.

---

## Kesimpulan
**Praktikum ini bertujuan agar mahasiswa memahami pemisahan mode eksekusi (User vs. Kernel). User program adalah pemohon, dan kernel adalah pelaksana.**

---

## Quiz
1. Apa fungsi utama system call dalam sistem operasi?    
   **Jawaban:**

   **Fungsi utama System Call adalah jembatan yang membuat OS dapat menjalankan aplikasi pengguna tanpa menyerahkan kendali penuh atau mengorbankan stabilitas sistem.**

2. Sebutkan 4 kategori system call yang umum digunakan.   
   **Jawaban:**
   **1. Kontrol Proses (Process Control)**

   **2. Manajemen Berkas (File Management)**

   **3. Manajemen Perangkat (Device Management)**

   **4. Informasi dan Komunikasi (Information & Communication)**

3. Mengapa system call tidak bisa dipanggil langsung oleh user program?  
   **Jawaban:**
    
   **System call tidak bisa dipanggil langsung oleh user program karena alasan utama yang berkaitan dengan keamanan, stabilitas sistem, dan privilese prosesor.**
 
---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?

   **Kesusahan menginstal Linux karena setiap kali akan mengetik perintah selalu langsung keluar dari Linux tersebut.**  
- Bagaimana cara Anda mengatasinya?
- 
  **menggunakan Cloud Shell: https://shell.cloud.google.com/**  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
