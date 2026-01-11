# Laporan Praktikum Minggu 14
**Topik:** Penyusunan Laporan Praktikum Format IMRAD (Studi Kasus: Analisis Performa Virtual Machine)

---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan 
- **NIM**   : 250202985
- **Kelas** : 1 IKRB

---

## 1. Pendahuluan (Introduction)
Virtualisasi merupakan teknologi fundamental dalam komputasi modern yang memungkinkan pembuatan versi virtual dari sumber daya komputasi, seperti sistem operasi, server, atau perangkat penyimpanan. Dengan menggunakan *Hypervisor* (seperti VirtualBox atau VMware), satu komputer fisik (*Host OS*) dapat menjalankan beberapa sistem operasi (*Guest OS*) secara bersamaan dalam lingkungan yang terisolasi [1].

Efisiensi virtualisasi sangat bergantung pada alokasi sumber daya perangkat keras, khususnya CPU dan RAM. Ketidaktepatan dalam mengalokasikan sumber daya dapat menyebabkan *bottleneck* performa, baik pada sisi *Guest* maupun *Host*. Selain aspek performa, virtualisasi juga menawarkan mekanisme keamanan melalui isolasi (*sandboxing*), di mana kerusakan pada sistem tamu tidak mempengaruhi sistem tuan rumah.

**Tujuan Eksperimen:**
Praktikum ini bertujuan untuk mengevaluasi dampak perubahan alokasi memori (RAM) terhadap kinerja sistem operasi Ubuntu yang berjalan di dalam Virtual Machine, serta memvalidasi mekanisme isolasi keamanan sistem.

---

## 2. Metode (Methods)
Eksperimen dilakukan menggunakan perangkat lunak virtualisasi Tipe 2 (*Hosted Hypervisor*). Berikut adalah spesifikasi lingkungan uji dan langkah-langkah yang dilakukan:

**A. Lingkungan Uji**
- **Software Virtualisasi:** Oracle VirtualBox
- **Guest OS:** Ubuntu Linux 24.04 LTS
- **Alat Ukur:** Terminal Linux (`free -h`, `uname -a`, `whoami`) dan System Monitor.

**B. Skenario Pengujian**
Pengujian dilakukan dengan membandingkan dua konfigurasi sumber daya (*resource*) yang berbeda pada beban kerja yang sama:
1. **Skenario A (High Resource):** Alokasi RAM 4 GB, CPU 2 Core.
2. **Skenario B (Low Resource):** Alokasi RAM 2 GB, CPU 1 Core.

**C. Prosedur Eksperimen**
1. Melakukan instalasi Ubuntu pada VirtualBox.
2. Menjalankan perintah dasar (`uname -a`) untuk memverifikasi kernel dan arsitektur.
3. Memberikan beban kerja (*stress test*) dengan membuka 5 *tab* Firefox (YouTube dan GitHub) secara bersamaan.
4. Mencatat penggunaan memori menggunakan perintah `free -h` dan mengamati responsivitas sistem (UI *latency* atau *lag*) pada kedua skenario.

---

## 3. Hasil (Results)
Berdasarkan eksperimen yang dilakukan pada kedua skenario, diperoleh data penggunaan sumber daya sebagai berikut:

**Tabel 1. Perbandingan Performa VM Berdasarkan Alokasi RAM**

| Parameter | Skenario A (4 GB RAM) | Skenario B (2 GB RAM) |
| :--- | :--- | :--- |
| **Total Memori Terdeteksi** | 3.8 Gi | 2.0 Gi |
| **Memori Terpakai (Load)** | 3.3 GB (79.2%) | 1.9 GB (97.2%) |
| **Status Aplikasi (Firefox)** | Responsif / Lancar | *Not Responding* / *Lag* Parah |
| **Kestabilan Sistem** | Stabil | Tidak Stabil |

**Visualisasi Hasil:**

*Gambar 1. Hasil monitoring pada Skenario A (RAM 4GB). Sistem berjalan lancar meski penggunaan memori mencapai 79%.*
![Screenshot Skenario 4GB](./screenshots/os_guest_running.jpeg)

*Gambar 2. Hasil monitoring pada Skenario B (RAM 2GB). Sistem mengalami kemacetan saat memori hampir penuh.*
![Screenshot Skenario 2GB](./screenshots/RAM%202%20GB.jpeg)

---

## 4. Pembahasan (Discussion)
Berdasarkan data pada Tabel 1, terlihat korelasi langsung antara alokasi sumber daya dan kinerja sistem.

1. **Manajemen Memori:** Pada Skenario A, beban kerja membutuhkan sekitar 3.3 GB RAM. Karena kapasitas tersedia adalah 4 GB, sistem operasi *Guest* dapat menampung seluruh proses aktif di dalam memori fisik (RAM) tanpa perlu melakukan *swapping* secara agresif ke disk. Hal ini menjaga sistem tetap responsif. Sebaliknya, pada Skenario B, kapasitas 2 GB tidak mencukupi untuk beban kerja yang sama. Hal ini memaksa OS untuk melakukan *paging* atau *swapping* berlebihan, yang menyebabkan penurunan performa drastis dan aplikasi menjadi *not responding*.

2. **Peran Hypervisor:**
   VirtualBox berhasil menerjemahkan instruksi dari *Guest OS* ke *Host OS*. Ketika resource diturunkan, Hypervisor membatasi akses *Guest* sesuai konfigurasi, membuktikan bahwa Hypervisor memegang kendali penuh atas manajemen sumber daya [2].

3. **Keamanan (Isolation):**
   Selama pengujian, meskipun *Guest OS* mengalami *hang* atau *crash* pada Skenario B, sistem operasi utama (*Host*) tetap berjalan normal tanpa gangguan. Ini memvalidasi konsep *sandboxing*, di mana lingkungan virtual terisolasi sepenuhnya dari lingkungan fisik.

---

## 5. Kesimpulan
Berdasarkan praktikum yang telah dilakukan, dapat disimpulkan bahwa:
1. Kinerja Virtual Machine berbanding lurus dengan ketersediaan sumber daya fisik; alokasi RAM yang di bawah kebutuhan beban kerja akan menyebabkan degradasi performa yang signifikan.
2. Mekanisme virtualisasi efektif menyediakan lapisan keamanan melalui isolasi, di mana kegagalan pada sistem tamu tidak merusak sistem tuan rumah.
3. Format pelaporan IMRAD membantu menyajikan data teknis perubahan performa ini secara terstruktur dan logis.

---

## Quiz (Minggu 14)
**1. Mengapa format IMRAD membantu membuat laporan praktikum lebih ilmiah dan mudah dievaluasi?**
Format IMRAD memberikan struktur logis yang standar (Pendahuluan, Metode, Hasil, Diskusi). Hal ini memudahkan pembaca atau pengevaluasi untuk menavigasi laporan: memahami konteks masalah di awal, memverifikasi cara pengujian di bagian metode, melihat data objektif di bagian hasil, dan memahami interpretasi penulis di bagian diskusi. Struktur ini juga memudahkan replikasi eksperimen oleh orang lain.

**2. Apa perbedaan antara bagian Hasil dan Pembahasan?**
- **Hasil (Results):** Bagian ini menyajikan data mentah, fakta, tabel, atau grafik yang didapat dari eksperimen secara objektif **tanpa** opini atau interpretasi. Contoh: "RAM terpakai 97%".
- **Pembahasan (Discussion):** Bagian ini berisi interpretasi, analisis, dan argumentasi penulis terhadap data tersebut. Bagian ini menjelaskan **"mengapa"** hasil tersebut terjadi dan kaitannya dengan teori. Contoh: "RAM terpakai 97% menyebabkan sistem melambat karena terjadi proses *thrashing*."

**3. Mengapa sitasi dan daftar pustaka penting, bahkan untuk laporan praktikum?**
Sitasi penting untuk menghargai karya intelektual orang lain (menghindari plagiarisme), memberikan validitas pada argumen yang disampaikan (berlandaskan teori yang sudah ada), serta memungkinkan pembaca untuk melacak sumber asli informasi guna pendalaman lebih lanjut.

---
## Daftar Pustaka
1. A. Silberschatz, P. B. Galvin, and G. Gagne, *Operating System Concepts*, 10th ed. Hoboken, NJ: Wiley, 2018.
2. Oracle, "Oracle VM VirtualBox User Manual," *VirtualBox.org*, 2024. [Online]. Available: https://www.virtualbox.org/manual/.

---
