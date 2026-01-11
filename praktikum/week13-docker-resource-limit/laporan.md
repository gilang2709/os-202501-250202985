
# Laporan Praktikum Minggu 13
Topik: Docker – Resource Limit (CPU & Memori)

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
1. **Persiapan Lingkungan**

   - Pastikan Docker terpasang dan berjalan.
   - Verifikasi:
     ```bash
     docker version
     docker ps
     ```

2. **Membuat Aplikasi/Skrip Uji**

   Buat program sederhana di folder `code/` (bahasa bebas) yang:
   - Melakukan komputasi berulang (untuk mengamati limit CPU), dan/atau
   - Mengalokasikan memori bertahap (untuk mengamati limit memori).

3. **Membuat Dockerfile**

   - Tulis `Dockerfile` untuk menjalankan program uji.
   - Build image:
     ```bash
     docker build -t week13-resource-limit .
     ```

4. **Menjalankan Container Tanpa Limit**

   - Jalankan container normal:
     ```bash
     docker run --rm week13-resource-limit
     ```
   - Catat output/hasil pengamatan.

5. **Menjalankan Container Dengan Limit Resource**

   Jalankan container dengan batasan resource (contoh):
   ```bash
   docker run --rm --cpus="0.5" --memory="256m" week13-resource-limit
   ```
   Catat perubahan perilaku program (mis. lebih lambat, error saat memori tidak cukup, dll.).

6. **Monitoring Sederhana**

   - Jalankan container (tanpa `--rm` jika perlu) dan amati penggunaan resource:
     ```bash
     docker stats
     ```
   - Ambil screenshot output eksekusi dan/atau `docker stats`.

7. **Commit & Push**

   ```bash
   git add .
   git commit -m "Minggu 13 - Docker Resource Limit"
   git push origin main
   ```

---

## Kode / Perintah
Tuliskan potongan kode atau perintah utama:
1. Struktur File
```bash
praktikum/week13-docker-resource-limit/
├─ code/
│  ├─ app.py
│  └─ Dockerfile
├─ screenshots/
│  ├─ docker-256mb.png
|  ├─ docker-build.png
|  └─ docker-limited.png
└─ laporan.md
```
2. app.py
```bash
import os
import time
import sys

def game():
    print("====================================================")
    print(f"   GAME SURVIVAL RESOURCE (PID: {os.getpid()})")
    print("====================================================")
    print("Aturan: Setiap Level akan memakan +50MB RAM.")
    print("Jika RAM penuh (melebihi limit Docker), game akan CRASH.\n")

    # --- TAHAP 1: MEMORY TEST (Loading Levels) ---
    print("--- [TAHAP 1] Memuat Asset & Texture ---")
    ram_storage = []
    
    try:
        for level in range(1, 11):
            print(f"Memuat Level {level}... | Total RAM digunakan: {level * 50} MB")
            
            # Alokasi 50MB per level
            level_data = bytearray(50 * 1024 * 1024) 
            ram_storage.append(level_data)
            
            # Jeda sebentar agar pergerakan 'docker stats' terlihat natural
            time.sleep(1)

        print("\n Berhasil! Semua Level (500MB RAM) termuat sempurna.")

    except MemoryError:
        print("\n GAME CRASHED! (Force Close)")
        print("Penyebab: Out Of Memory (OOM).")
        print("Docker membatasi penggunaan RAM untuk container ini.")
        sys.exit(1)
    except Exception as e:
        # Pada banyak kasus Docker, jika kena limit memori, container langsung mati 
        # tanpa sempat masuk ke blok except ini (Killed).
        print(f"\nTerjadi kesalahan sistem: {e}")
        sys.exit(1)

    # --- TAHAP 2: CPU TEST (Rendering Graphics) ---
    print("\n--- [TAHAP 2] Rendering Grafik Game ---")
    print("CPU dipaksa bekerja keras untuk menghitung frame...")
    
    start_time = time.time()
    total_frames = 0
    duration = 5 # Durasi rendering 5 detik

    while time.time() - start_time < duration:
        # Simulasi beban kerja berat (hitung kuadrat)
        _ = [x**2 for x in range(5000)]
        total_frames += 1
    
    avg_fps = total_frames / duration
    print(f" Hasil Rendering:")
    print(f"   -> Total Frame yang diproses: {total_frames}")
    print(f"   -> Rata-rata Performa: {avg_fps:.2f} FPS")
    
    if avg_fps < 500: # Angka ambang batas ini hanya contoh
        print("   -> Status: Performa Lambat (CPU dilimit).")
    else:
        print("   -> Status: Performa Lancar (CPU tanpa limit).")

    print("\n--- GAME SELESAI ---")

if __name__ == "__main__":
    game()
```
3. Dockerfile
```bash
FROM python:3.14-alpine

WORKDIR /app

COPY app.py .

ENV PYTHONUNBUFFERED=1

CMD ["python", "app.py"]
```

---

## Hasil Eksekusi
Sertakan screenshot hasil percobaan atau diagram:
1. Instalasi Docker
![Screenshot hasil](./screenshots/Docker-instal.png)
2. Membuat Dockerfile
![Screenshot hasil](./screenshots/docker%20build%20-t%20week13-resource-limit%20..png)
3. Menjalankan Container Tanpa Limit
![Screenshot hasil](./screenshots/docker%20run%20--rm%20week13-resource-limit.png)
5. Menjalankan Container Dengan Limit Resource
![Screenshot hasil](./screenshots/docker%20run%20--rm%20--cpus=0.5%20--memory=256m%20week13-resource-limit.png)

---

## Analisis
Analisis Skenario Tanpa Limit
Pada eksekusi normal, program berhasil melewati seluruh tahap (Level 1 hingga 10) dan mencapai penggunaan memori sebesar 500 MB.
   * Perilaku RAM: Penggunaan memori meningkat stabil 50 MB setiap detik tanpa hambatan.
   * Perilaku CPU: Pada tahap rendering, CPU mampu memproses frame dengan kecepatan maksimal (asumsi: >1000 FPS).
   * Kesimpulan: Tanpa batasan, Docker mengizinkan container menggunakan sumber daya sebanyak mungkin yang tersedia pada sistem host.


---

## Kesimpulan
1. Docker Resource Limit sangat efektif untuk menjaga stabilitas sistem dengan mencegah satu container (proses) mendominasi penggunaan CPU dan Memori.

2. Mekanisme cgroups pada kernel Linux bertindak sebagai polisi resource yang memantau dan membatasi penggunaan sesuai parameter --memory dan --cpus.

3. Penggunaan image berbasis Alpine Linux (python:3.14-alpine) membuat overhead container menjadi sangat kecil, sehingga pengamatan resource limit menjadi lebih akurat.

---

## Quiz
1. Mengapa container perlu dibatasi CPU dan memori? 
**Jawaban:** 
Untuk mencegah fenomena Noisy Neighbor, di mana satu container yang mengalami memory leak atau infinite loop menghabiskan seluruh sumber daya host yang berakibat pada kegagalan layanan container lain dan sistem host itu sendiri.

2. Apa perbedaan VM dan container dalam konteks isolasi resource? 
**Jawaban:** 
VM mengisolasi resource pada level perangkat keras (hardware) melalui Hypervisor (alokasi tetap), sedangkan Container mengisolasi pada level sistem operasi menggunakan cgroups dan namespaces (berbagi kernel host, alokasi lebih fleksibel).

3. Apa dampak limit memori terhadap aplikasi yang boros memori? 
**Jawaban:** 
Aplikasi akan mengalami penghentian paksa oleh kernel melalui mekanisme OOM (Out Of Memory) Killer, atau jika di dalam program ditangani dengan baik, akan memicu Exception MemoryError.

---

## Refleksi Diri
Tuliskan secara singkat:
- Apa bagian yang paling menantang minggu ini?  
- Bagaimana cara Anda mengatasinya?  

---

**Credit:**  
_Template laporan praktikum Sistem Operasi (SO-202501) – Universitas Putra Bangsa_
