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