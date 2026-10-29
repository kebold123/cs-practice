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
    try:
        temp = float(temp)
    except:
        raise ValueError("Температура не является числом")
    
    if not city.strip() or not date.strip():
        raise ValueError("Город или дата пустая")
    
    return {"city": city, "temperature": temp, "date": date}

def average_by_city(records: list[dict]) -> dict:
    for data in records:
        print(data)

def warmest_city(records: list[dict]) -> str:
    pass

average_by_city(read_valid(["Азов;24.5;2026-07-01", "Азов;27.4;2026-07-05"]))