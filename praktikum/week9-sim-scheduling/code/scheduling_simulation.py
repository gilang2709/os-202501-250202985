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