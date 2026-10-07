import sys

def read_valid(lines: list[str]) -> list[dict]:
    data = []
    for line in lines:
        try:
            data.append(parse_record(line))
        except: pass
    return data

def parse_record(line: str) -> dict:
    parts = line.split(";")
    
    if len(parts) != 3:
        raise ValueError("Поля не три")
    
    city, temp, date = parts
    temp = float(temp)
    
    if not city or not date:
        raise ValueError("Город или дата пустая")
    
    return {"city": city, "temp": temp, "date": date}

def average_by_city(records: list[dict]) -> dict:
    pass

def warmest_city(records: list[dict]) -> str:
    pass

