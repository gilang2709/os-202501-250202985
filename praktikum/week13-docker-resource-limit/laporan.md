
# Laporan Praktikum Minggu 13
Topik: [Tuliskan judul topik, misalnya "Arsitektur Sistem Operasi dan Kernel"]

---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan 
- **NIM**   : 250202985
- **Kelas** : 1 IKRB

---

## Tujuan
1. Menulis Dockerfile sederhana untuk sebuah aplikasi/skrip.
2. Membangun image dan menjalankan container.
3. Menjalankan container dengan pembatasan **CPU** dan **memori**.
4. Mengamati dan menjelaskan perbedaan eksekusi container dengan dan tanpa limit resource.
5. Menyusun laporan praktikum secara runtut dan sistematis.
---

## Dasar Teori
1. Containerization & Docker: Docker menggunakan virtualisasi tingkat sistem operasi. Berbeda dengan Virtual Machine (VM) yang meniru perangkat keras, container berbagi kernel host yang sama namun berjalan di ruang pengguna (userspace) yang terisolasi.

2. Control Groups (cgroups): Ini adalah fitur kernel Linux yang memungkinkan Docker membatasi, mengukur, dan mengisolasi penggunaan sumber daya (CPU, memori, I/O disk) dari kumpulan proses. cgroups memastikan satu container tidak menghabiskan seluruh sumber daya host.

3. Namespaces: Fitur kernel yang memisahkan view sistem (seperti Process ID, Network, Mount point) sehingga container merasa berjalan sendiri di sistem operasi, padahal berbagi kernel yang sama.

4. OOM Killer (Out of Memory): Mekanisme perlindungan kernel. Jika container mencoba menggunakan memori melebihi batas yang ditentukan (--memory), kernel akan mematikan proses di dalam container tersebut untuk menjaga stabilitas sistem.
---

## Langkah Praktikum
1. Langkah-langkah yang dilakukan.  
2. Perintah yang dijalankan.  
3. File dan kode yang dibuat.  
4. Commit message yang digunakan.

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
uname -a
lsmod | head
dmesg | head
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](screenshots/example.png)

---

## Analisis
- Jelaskan makna hasil percobaan.  
- Hubungkan hasil dengan teori (fungsi kernel, system call, arsitektur OS).  
- Apa perbedaan hasil di lingkungan OS berbeda (Linux vs Windows)?  

---

## Kesimpulan
Tuliskan 2–3 poin kesimpulan dari praktikum ini.

---

## Quiz
1. [Pertanyaan 1]  
   **Jawaban:**  
2. [Pertanyaan 2]  
   **Jawaban:**  
3. [Pertanyaan 3]  
   **Jawaban:**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
