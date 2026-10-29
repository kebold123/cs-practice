import sys
from stats import average_by_city, parse_record, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid_records = []
    corrupted_count = 0
    
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            corrupted_count += 1
            
    print(len(valid_records))
    print(corrupted_count)
    
    if valid_records:
        best_city = warmest_city(valid_records)
        averages = average_by_city(valid_records)
        
        print(f"{averages[best_city]:.1f}")
    else:
        print("0.0")

if __name__ == "__main__":
    main()