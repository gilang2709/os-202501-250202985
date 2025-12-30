def print_table(title, reference_string, history, faults):
    print(f"\n{'='*50}")
    print(f"{title.center(50)}")
    print(f"{'='*50}")
    print(f"{'No':<4} | {'Page':<5} | {'Status':<8} | {'Isi Frame':<15}")
    print("-" * 50)
    
    for i, (page, status, frame) in enumerate(history):
        frame_str = str(frame).replace('[', '[ ').replace(']', ' ]').replace(',', '')
        print(f"{i+1:<4} | {page:<5} | {status:<8} | {frame_str:<15}")
    
    print("-" * 50)
    print(f"Total Page Fault: {faults}")

def simulate():
    pages = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2]
    capacity = 3
    
    # --- SIMULASI FIFO ---
    fifo_memory = []
    fifo_history = []
    fifo_faults = 0
    
    for page in pages:
        if page not in fifo_memory:
            status = "MISS"
            if len(fifo_memory) < capacity:
                fifo_memory.append(page)
            else:
                fifo_memory.pop(0)
                fifo_memory.append(page)
            fifo_faults += 1
        else:
            status = "HIT"
        fifo_history.append((page, status, list(fifo_memory)))
    
    print_table("SIMULASI FIFO (First-In First-Out)", pages, fifo_history, fifo_faults)

    # --- SIMULASI LRU ---
    lru_memory = []
    lru_history = []
    lru_faults = 0
    
    for page in pages:
        if page not in lru_memory:
            status = "MISS"
            if len(lru_memory) < capacity:
                lru_memory.append(page)
            else:
                lru_memory.pop(0)
                lru_memory.append(page)
            lru_faults += 1
        else:
            status = "HIT"
            # Move to end (most recently used)
            lru_memory.remove(page)
            lru_memory.append(page)
        lru_history.append((page, status, list(lru_memory)))

    print_table("SIMULASI LRU (Least Recently Used)", pages, lru_history, lru_faults)

if __name__ == "__main__":
    simulate()