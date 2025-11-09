
# Laporan Praktikum Minggu 6
Topik: Penjadwalan CPU – Round Robin (RR) dan Priority Scheduling
---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan
- **NIM**   : 250202985  
- **Kelas** : 1 IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Menghitung *waiting time* dan *turnaround time* pada algoritma RR dan Priority.  
2. Menyusun tabel hasil perhitungan dengan benar dan sistematis.  
3. Membandingkan performa algoritma RR dan Priority.  
4. Menjelaskan pengaruh *time quantum* dan prioritas terhadap keadilan eksekusi proses.  
5. Menarik kesimpulan mengenai efisiensi dan keadilan kedua algoritma. 

---

## Dasar Teori
1. Penjadwalan CPU menentukan urutan eksekusi proses agar penggunaan CPU efisien dan adil.

2. Round Robin (RR) menggunakan time quantum tetap; proses dijalankan bergantian dan dikembalikan ke antrian jika belum selesai. Menekankan keadilan waktu eksekusi.

3. Priority Scheduling mengeksekusi proses berdasarkan tingkat prioritas. Bisa preemptive atau non-preemptive, dengan risiko starvation yang dapat diatasi dengan aging.

4. Indikator kinerja:
- Waiting Time (WT) = waktu tunggu proses di antrian.
- Turnaround Time (TAT) = waktu total sejak tiba hingga selesai.

5. Analisis:
- Pada RR, time quantum memengaruhi efisiensi dan overhead.
- Pada Priority, perbedaan prioritas memengaruhi keadilan dan waktu respon sistem.

---

## Langkah Praktikum
1. **Siapkan Data Proses**
   Gunakan contoh data berikut (boleh dimodifikasi sesuai kebutuhan):
   | Proses | Burst Time | Arrival Time | Priority |
   |:--:|:--:|:--:|:--:|
   | P1 | 5 | 0 | 2 |
   | P2 | 3 | 1 | 1 |
   | P3 | 8 | 2 | 4 |
   | P4 | 6 | 3 | 3 |

2. **Eksperimen 1 – Round Robin (RR)**
   - Gunakan *time quantum (q)* = 3.  
   - Hitung *waiting time* dan *turnaround time* untuk tiap proses.  
   - Simulasikan eksekusi menggunakan Gantt Chart (manual atau spreadsheet).  
     ```
     | P1 | P2 | P3 | P4 | P1 | P3 | ...
     0    3    6    9   12   15   18  ...
     ```
   - Catat sisa *burst time* tiap putaran.

3. **Eksperimen 2 – Priority Scheduling (Non-Preemptive)**
   - Urutkan proses berdasarkan nilai prioritas (angka kecil = prioritas tinggi).  
   - Lakukan perhitungan manual untuk:
     ```
     WT[i] = waktu mulai eksekusi - Arrival[i]
     TAT[i] = WT[i] + Burst[i]
     ```
   - Buat tabel perbandingan hasil RR dan Priority.

4. **Eksperimen 3 – Analisis Variasi Time Quantum (Opsional)**
   - Ubah *quantum* menjadi 2 dan 5.  
   - Amati perubahan nilai rata-rata *waiting time* dan *turnaround time*.  
   - Buat tabel perbandingan efek *quantum*.

5. **Eksperimen 4 – Dokumentasi**
   - Simpan semua hasil tabel dan screenshot ke:
     ```
     praktikum/week6-scheduling-rr-priority/screenshots/
     ```
   - Buat tabel perbandingan seperti berikut:

     | Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
     |------------|------------------|----------------------|------------|-------------|
     | RR | ... | ... | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
     | Priority | ... | ... | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

6. **Commit & Push**
   ```bash
   git add .
   git commit -m "Minggu 6 - CPU Scheduling RR & Priority"
   git push origin main
   ```


---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
WT[i] = waktu mulai eksekusi - Arrival[i]
TAT[i] = WT[i] + Burst[i]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:

![Screenshot hasil](./screenshots/Eksperimen%201%20RR.png)
![Screenshot hasil](./screenshots/Eksperimen%202%20Priority%20Scheduling.png)

---

## Eksperimen 1
- Tabel Perhitungan

![Screenshot hasil](./screenshots/Eksperimen%201%20RR.png)

- Gantt Chart
```bash
| P1 | P2 | P3 | P4 | P1 | P3 | P4 | P4|
0    3    6    9   12   15   18   21  24
```

---

## Eksperimen 2
- Tabel Perhitungan

![Screenshot hasil](./screenshots/Eksperimen%202%20Priority%20Scheduling.png)

- Gantt Chart
```bash
| P1 | P2 | P4 | P3 |
0    5    8   14   22 
```

---

## Tabel Perbandingan

| Algoritma | Avg Waiting Time | Avg Turnaround Time | Kelebihan | Kekurangan |
|------------|------------------|----------------------|------------|-------------|
| RR | 11,75 | 12,5 | Adil terhadap semua proses | Tidak efisien jika quantum tidak tepat |
| Priority | 5,25 | 10,75 | Efisien untuk proses penting | Potensi *starvation* pada prioritas rendah |

---

## Analisis
- Bandingkan performa dan jelaskan pengaruh time quantum serta prioritas.
  - Perbandingan performa
    -  Priority Scheduling menghasilkan kinerja rata-rata lebih cepat (nilai WT dan TAT rata-rata lebih rendah). Ini menunjukkan bahwa sistem menyelesaikan pekerjaan dengan lebih efisien jika fokus pada proses penting.
    -  Round Robin menghasilkan kinerja rata-rata yang lebih lambat, tetapi menawarkan distribusi waktu tunggu yang lebih adil di antara semua proses.
   -  Pengaruh Time Quantum (q) adalah faktor penentu utama dalam kinerja RR dan keadilan sistem.
   -  Prioritas menentukan urutan eksekusi, yang berdampak besar pada WT dan TAT individu.

---

## Kesimpulan
1. Round Robin = Adil, tetapi Kurang Efisien:Round Robin (RR) adalah algoritma yang adil karena setiap proses mendapat jatah waktu yang sama. Namun, keadilan ini dibayar dengan kinerja rata-rata yang lebih lambat (WT dan TAT rata-rata lebih tinggi) dibandingkan Priority Scheduling.
2. Prioritas = Efisien, tetapi Tidak Adil:
Priority Scheduling sangat efisien (nilai WT dan TAT rata-rata rendah) karena menyelesaikan tugas-tugas penting lebih dulu. Namun, kelemahannya adalah tidak adil; proses dengan prioritas rendah menunggu terlalu lama (berpotensi Starvation).
3. Kunci RR adalah Time Quantum (q):
Kinerja RR sangat tergantung pada penentuan Time Quantum (q).
     - Jika q terlalu kecil, sistem boros karena terlalu banyak Context Switch (perpindahan proses).
     - Jika q terlalu besar, RR menjadi mirip FCFS (First-Come, First-Served), sehingga proses kecil harus menunggu lama dan mengurangi keadilan. Pemilihan q yang tepat adalah kunci efisiensi RR.

---

## Quiz
1. Apa perbedaan utama antara Round Robin dan Priority Scheduling? 

     - **Round Robin (RR): Algoritma ini dirancang untuk menciptakan keadilan dan respons yang cepat. CPU berputar di antara semua proses yang siap, memberikan jatah waktu (quantum) yang singkat kepada masing-masing. Ini menjamin bahwa tidak ada proses yang menunggu terlalu lama untuk mendapatkan CPU.**
  
     - **Priority Scheduling: Algoritma ini fokus pada kepentingan proses. Proses yang dianggap lebih penting (prioritas tinggi) mendapatkan akses CPU terlebih dahulu. Kelemahannya adalah jika banyak proses prioritas tinggi terus berdatangan, proses prioritas rendah bisa kelaparan (starvation) dan tidak pernah dieksekusi.** 
 
2. Apa pengaruh besar/kecilnya time quantum terhadap performa sistem?

   - **Jika quantum sangat kecil, sistem akan menyerupai multitasking yang sempurna di mana semua proses berjalan bersamaan (disebut Processor Sharing). Namun, ini datang dengan biaya overhead yang besar.**

   - **Jika quantum sangat besar (melebihi burst time proses), Round Robin efektif berubah menjadi FCFS, karena setiap proses kemungkinan selesai sebelum time quantum habis.**
3. Mengapa algoritma Priority dapat menyebabkan starvation?

     -  **Algoritma Priority dapat menyebabkan starvation karena sifat dasarnya yang hanya memprioritaskan proses dengan nilai prioritas tertinggi dan secara konsisten menunda eksekusi proses dengan prioritas yang lebih rendah.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
