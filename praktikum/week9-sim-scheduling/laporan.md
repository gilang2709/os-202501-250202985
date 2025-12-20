
# Laporan Praktikum Minggu [9]
Topik: [Simulasi Algoritma Penjadwalan CPU]

---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan  
- **NIM**   : 250202985  
- **Kelas** : 1IKRB

---

## Tujuan
Setelah menyelesaikan tugas ini, mahasiswa mampu:
1. Membuat program simulasi algoritma penjadwalan FCFS dan/atau SJF.  
2. Menjalankan program dengan dataset uji yang diberikan atau dibuat sendiri.  
3. Menyajikan output simulasi dalam bentuk tabel atau grafik.  
4. Menjelaskan hasil simulasi secara tertulis.  
5. Mengunggah kode dan laporan ke Git repository dengan rapi dan tepat waktu.

---

## Dasar Teori
1. Definisi: Penjadwalan CPU adalah metode pengaturan antrean proses agar CPU tetap produktif. Simulasi ini bertujuan untuk mengukur efisiensi sistem melalui otomatisasi perhitungan waktu eksekusi.
2. Metrik Evaluasi: Efisiensi diukur menggunakan dua rumus utama:
   1. Turnaround Time (TAT): Waktu Selesai - Waktu Tiba ($TAT = FT - AT$).
   2. Waiting Time (WT): Waktu Tunggu selama di antrean ($WT = TAT - BT$).
3. Algoritma FCFS (First-Come, First-Served): Algoritma non-preemptive yang melayani proses berdasarkan urutan waktu kedatangan. Sederhana secara logika namun berisiko menyebabkan convoy effect.
4. Algoritma SJF (Shortest Job First): Algoritma yang memprioritaskan proses dengan durasi (Burst Time) terpendek. Metode ini paling efektif untuk meminimalkan rata-rata waktu tunggu (Average Waiting Time).

---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Buat dataset proses minimal berisi:

   | Proses | Arrival Time | Burst Time |
   |:--:|:--:|:--:|
   | P1 | 0 | 6 |
   | P2 | 1 | 8 |
   | P3 | 2 | 7 |
   | P4 | 3 | 3 |

2. **Implementasi Algoritma**

   Program harus:
   - Menghitung *waiting time* dan *turnaround time*.  
   - Mendukung minimal **1 algoritma (FCFS atau SJF non-preemptive)**.  
   - Menampilkan hasil dalam tabel.

3. **Eksekusi & Validasi**

   - Jalankan program menggunakan dataset uji.  
   - Pastikan hasil sesuai dengan perhitungan manual minggu sebelumnya.  
   - Simpan hasil eksekusi (screenshot).

4. **Analisis**

   - Jelaskan alur program.  
   - Bandingkan hasil simulasi dengan perhitungan manual.  
   - Jelaskan kelebihan dan keterbatasan simulasi.

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 9 - Simulasi Scheduling CPU"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import csv
import os

def load_dataset(file_path):
    dataset = []
    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                dataset.append({
                    'Process': row['Proses'],
                    'AT': int(row['Arrival Time']),
                    'BT': int(row['Burst Time'])
                })
        return dataset
    except FileNotFoundError:
        print(f"Error: File {file_path} tidak ditemukan.")
        return None

def simulate_fcfs(processes):
    # Urutkan berdasarkan Arrival Time (AT)
    processes.sort(key=lambda x: x['AT'])
    
    current_time = 0
    results = []
    
    for p in processes:
        # Jika CPU idle (waktu sekarang < waktu tiba proses)
        if current_time < p['AT']:
            current_time = p['AT']
            
        start_time = current_time
        finish_time = start_time + p['BT']
        turnaround_time = finish_time - p['AT']
        waiting_time = turnaround_time - p['BT']
        
        results.append({
            'Proses': p['Process'],
            'AT': p['AT'],
            'BT': p['BT'],
            'FT': finish_time,
            'TAT': turnaround_time,
            'WT': waiting_time
        })
        
        current_time = finish_time
        
    return results

def display_results(results):
    print("\n" + "="*55)
    print(f"{'Proses':<8} | {'AT':<4} | {'BT':<4} | {'FT':<4} | {'TAT':<5} | {'WT':<4}")
    print("-" * 55)
    
    total_tat = 0
    total_wt = 0
    
    for r in results:
        print(f"{r['Proses']:<8} | {r['AT']:<4} | {r['BT']:<4} | {r['FT']:<4} | {r['TAT']:<5} | {r['WT']:<4}")
        total_tat += r['TAT']
        total_wt += r['WT']
        
    avg_tat = total_tat / len(results)
    avg_wt = total_wt / len(results)
    
    print("-" * 55)
    print(f"Average Turnaround Time: {avg_tat:.2f}")
    print(f"Average Waiting Time   : {avg_wt:.2f}")
    print("="*55 + "\n")

if __name__ == "__main__":
    # Path dataset sesuai struktur folder praktikum
    csv_path = os.path.join(os.path.dirname(__file__), 'dataset.csv')
    
    print("Simulasi Penjadwalan CPU - FCFS")
    data = load_dataset(csv_path)
    
    if data:
        hasil = simulate_fcfs(data)
        display_results(hasil)
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/./Simulasi%20Penjadwalan%20CPU%20-%20FCFS.png)

---

## Analisis
* Alur Program: Program membaca CSV, mengurutkan data berdasarkan waktu tiba, menghitung waktu selesai setiap proses secara sekuensial, dan mengkalkulasi selisih waktu untuk mendapatkan TAT dan WT.
* Perbandingan Manual: Hasil simulasi identik dengan perhitungan manual, membuktikan logika program valid sesuai teori.
* Kelebihan & Kekurangan: Simulasi sangat cepat untuk dataset besar dan akurat secara matematis, namun memiliki keterbatasan karena mengabaikan overhead context switching dan interupsi pada sistem operasi nyata.
---

## Kesimpulan
1. Otomatisasi simulasi meningkatkan akurasi dan kecepatan evaluasi algoritma penjadwalan.

2. Algoritma FCFS sangat bergantung pada urutan kedatangan, di mana proses yang datang pertama selalu dilayani pertama tanpa mempedulikan durasi eksekusi.

3. Simulasi merupakan alat bantu penting untuk memprediksi performa sistem sebelum diimplementasikan pada lingkungan produksi.
---

## Quiz
1. [Mengapa simulasi diperlukan untuk menguji algoritma scheduling?]  
   **Jawaban: Untuk mengevaluasi efisiensi algoritma tanpa mengganggu sistem nyata dan memprediksi hasil pada berbagai skenario dataset secara cepat.**  
2. [Apa perbedaan hasil simulasi dengan perhitungan manual jika dataset besar? ]  
   **Jawaban: Simulasi memberikan akurasi tinggi dan kecepatan pemrosesan, sedangkan perhitungan manual sangat berisiko terhadap kesalahan manusia (human error).**  
3. [Algoritma mana yang lebih mudah diimplementasikan? Jelaskan.]  
   **Jawaban: FCFS, karena logikanya hanya menggunakan prinsip antrean sederhana (FIFO) tanpa memerlukan pengecekan ulang atau pengurutan burst time di tengah proses berjalan.**  

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
