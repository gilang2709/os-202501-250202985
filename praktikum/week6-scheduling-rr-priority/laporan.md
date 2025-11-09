
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
