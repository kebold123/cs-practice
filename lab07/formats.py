import json

def csv_to_records(text: str) -> list[dict]:
    lines = text.strip().split("\n")
    if not lines or lines == [""]:
        return []
    
    headers = [h.strip() for h in lines[0].split(",")]
    records = []
    
    for line in lines[1:]:
        if not line.strip():
            continue
        values = [v.strip() for v in line.split(",")]
        record = {}
        for i, header in enumerate(headers):
            record[header] = values[i] if i < len(values) else ""
        records.append(record)
    
    return records