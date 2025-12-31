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