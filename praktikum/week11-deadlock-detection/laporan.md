
# Laporan Praktikum Minggu 11
Topik: Simulasi dan Deteksi Deadlock


---

## Identitas
- **Nama**  : Fatkhurrohman Gilang Ramadhan  
- **NIM**   : 250202985
- **Kelas** : 1 IKRB

---

## Tujuan
1. Membuat program sederhana untuk mendeteksi deadlock.  
2. Menjalankan simulasi deteksi deadlock dengan dataset uji.  
3. Menyajikan hasil analisis deadlock dalam bentuk tabel.  
4. Memberikan interpretasi hasil uji secara logis dan sistematis.  
5. Menyusun laporan praktikum sesuai format yang ditentukan.


---

## Dasar Teori
Deadlock adalah kondisi di mana sekumpulan proses saling menunggu satu sama lain untuk melepaskan sumber daya (resource), sehingga tidak ada satupun proses yang dapat berjalan.

Empat kondisi yang harus terpenuhi agar deadlock terjadi (Coffman Conditions):
1.  **Mutual Exclusion:** Sumber daya hanya bisa digunakan oleh satu proses pada satu waktu.
2.  **Hold and Wait:** Proses menahan sumber daya sambil menunggu sumber daya lain.
3.  **No Preemption:** Sumber daya tidak bisa diambil paksa dari proses yang sedang memegangnya.
4.  **Circular Wait:** Terdapat rantai proses $\{P_0, P_1, \dots, P_n\}$ di mana $P_0$ menunggu $P_1$, $P_1$ menunggu $P_2$, dan $P_n$ menunggu $P_0$.

Untuk mendeteksi deadlock pada sistem dengan *single instance resource*, kita dapat menggunakan **Wait-for Graph**. Jika terdapat siklus (*cycle*) dalam graf tersebut, maka sistem berada dalam kondisi deadlock.
---

## Langkah Praktikum
1. **Menyiapkan Dataset**

   Gunakan dataset sederhana yang berisi:
   - Daftar proses  
   - Resource Allocation  
   - Resource Request / Need

   Contoh tabel:

   | Proses | Allocation | Request |
   |:--:|:--:|:--:|
   | P1 | R1 | R2 |
   | P2 | R2 | R3 |
   | P3 | R3 | R1 |

2. **Implementasi Algoritma Deteksi Deadlock**

   Program minimal harus:
   - Membaca data proses dan resource.  
   - Menentukan apakah sistem berada dalam kondisi deadlock.  
   - Menampilkan proses mana saja yang terlibat deadlock.

3. **Eksekusi & Validasi**

   - Jalankan program dengan dataset uji.  
   - Validasi hasil deteksi dengan analisis manual/logis.  
   - Simpan hasil eksekusi dalam bentuk screenshot.

4. **Analisis Hasil**

   - Sajikan hasil deteksi dalam tabel (proses deadlock / tidak).  
   - Jelaskan mengapa deadlock terjadi atau tidak terjadi.  
   - Kaitkan hasil dengan teori deadlock (empat kondisi).

5. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 11 - Deadlock Detection"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
```bash
import csv
import os

def load_data(filename):
    """Membaca file CSV dan mengembalikan list dictionary."""
    data = []
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' tidak ditemukan di lokasi tersebut.")
        return []
    
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            clean_row = {k.strip(): v.strip() for k, v in row.items()}
            data.append(clean_row)
    return data

def detect_deadlock(data):
    """Mendeteksi siklus menggunakan Wait-For Graph."""
    # Petakan Resource ke Pemiliknya
    resource_owner = {row['Allocation']: row['Proses'] for row in data if row['Allocation'] != 'None'}
    
    # Bangun adjacency list (Siapa menunggu siapa)
    graph = {}
    for row in data:
        p_name = row['Proses']
        req = row['Request']
        graph[p_name] = []
        if req in resource_owner:
            graph[p_name].append(resource_owner[req])

    # Algoritma DFS untuk mencari Cycle
    def has_cycle(v, visited, stack, cycle_nodes):
        visited.add(v)
        stack.add(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                if has_cycle(neighbor, visited, stack, cycle_nodes):
                    cycle_nodes.add(v)
                    return True
            elif neighbor in stack:
                cycle_nodes.add(v)
                cycle_nodes.add(neighbor)
                return True
        stack.remove(v)
        return False

    visited = set()
    deadlocked = set()
    for node in graph:
        if node not in visited:
            temp_stack = set()
            has_cycle(node, visited, temp_stack, deadlocked)
    
    return list(deadlocked)

def main():
    print("=== SIMULASI DETEKSI DEADLOCK ===")
    
    # Mencari path absolut agar file CSV selalu ketemu
    base_path = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_path, 'dataset_deadlock.csv')

    data = load_data(file_path)
    if not data: return

    result = detect_deadlock(data)

    print("\n[HASIL ANALISIS]")
    if result:
        print(f"Sistem dalam keadaan DEADLOCK!")
        print(f"Proses yang terlibat: {', '.join(sorted(result))}")
    else:
        print("Sistem AMAN (Tidak ada deadlock).")

if __name__ == "__main__":
    main()
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
![Screenshot hasil](./screenshots/hasil_deteksi.png)

---

## Analisis
1. Wait-For Graph Construction:Program berhasil memetakan ketergantungan:
   * P1 memegang R1, meminta R2 (yang dipegang P2) $\rightarrow$ P1 menunggu P2.
   * P2 memegang R2, meminta R3 (yang dipegang P3) $\rightarrow$ P2 menunggu P3.
   * P3 memegang R3, meminta R1 (yang dipegang P1) $\rightarrow$ P3 menunggu P1.
2. Deteksi Deadlock:
Algoritma mendeteksi adanya siklus: P1 $\rightarrow$ P2 $\rightarrow$ P3 $\rightarrow$ P1.
Ini memenuhi syarat Circular Wait. Karena resource bersifat non-preemptable dan mutual exclusion (asumsi default sistem), maka kondisi ini dikonfirmasi sebagai Deadlock.
3. Proses Lain: Proses P4 dan P5 tidak terlibat dalam deadlock karena P4 meminta R5 (dipegang P5), namun P5 tidak meminta apapun (tidak menunggu), sehingga rantai terputus.
---

## Kesimpulan
1. Deteksi deadlock dapat dilakukan dengan memodelkan sistem sebagai Wait-for Graph.

2. Keberadaan siklus (cycle) dalam graf alokasi sumber daya tunggal (single instance) merupakan indikator pasti terjadinya deadlock.

3. Algoritma DFS efektif digunakan untuk menelusuri graf dan menemukan ketergantungan melingkar antar proses.

---

## Quiz
1. Apa perbedaan antara deadlock prevention, avoidance, dan detection?  
   **Jawaban:**
   * Prevention: Memastikan deadlock tidak akan pernah terjadi dengan cara merusak salah satu dari 4 kondisi Coffman (misal: melarang hold and wait).

   * Avoidance: Mengizinkan 4 kondisi terjadi, tetapi sistem menghitung setiap permintaan resource di awal (misal: Banker's Algorithm) untuk memastikan sistem selalu berada dalam Safe State.

   * Detection: Membiarkan deadlock terjadi, lalu sistem secara berkala memeriksa status resource untuk mendeteksi deadlock dan melakukan pemulihan (recovery).**  
2. Mengapa deteksi deadlock tetap diperlukan dalam sistem operasi?  
   **Jawaban:**
   * Karena prevention dan avoidance seringkali terlalu restriktif dan menurunkan throughput sistem (penggunaan resource jadi tidak maksimal). Deteksi memungkinkan sistem berjalan lebih bebas dan efisien, dengan risiko sesekali harus menangani deadlock jika benar-benar terjadi.  
3. Apa kelebihan dan kekurangan pendekatan deteksi deadlock?  
   **Jawaban:**  
   * Kelebihan: Utilisasi sumber daya lebih tinggi karena proses tidak dikekang di awal.

   * Kekurangan: Ada overhead komputasi untuk menjalankan algoritma deteksi secara berkala, dan proses pemulihan (seperti mematikan proses) bisa menyebabkan kehilangan data atau ketidakstabilan sistem.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
