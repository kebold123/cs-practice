def parse_record(line: str) -> dict:
    """
    Разбирает строку «город;температура;дата» в словарь.
    Учитывает лишние пробелы, пустые поля и неверный формат чисел.
    """
    if not line or not line.strip():
        raise ValueError("Пустая строка")

    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Строка должна содержать ровно 3 поля, разделенных ';'")

    city = parts[0].strip()
    temp_str = parts[1].strip()
    date = parts[2].strip()

    if not city or not date:
        raise ValueError("Город или дата не могут быть пустыми")

    temp_str = temp_str.replace(",", ".")

    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError(f"Некорректный формат температуры: '{parts[1]}'")

    return {"city": city, "temperature": temp, "date": date}


def read_valid(lines: list[str]) -> list[dict]:
    """
    Разбирает строки журнала. Молча пропускает пустые строки.
    Игнорирует некорректные записи (ошибки перехватываются снаружи в main.py).
    """
    valid_records = []
    for line in lines:
        if not line or not line.strip():
            continue
        try:
            record = parse_record(line)
            valid_records.append(record)
        except ValueError:
            pass
    return valid_records


def average_by_city(records: list[dict]) -> dict:
    """
    Вычисляет среднюю температуру по каждому городу,
    округлённую до десятых. Защищена от пустого списка.
    """
    if not records:
        return {}

    city_totals = {}
    city_counts = {}

    for rec in records:
        city = rec["city"]
        temp = rec["temperature"]
        city_totals[city] = city_totals.get(city, 0.0) + temp
        city_counts[city] = city_counts.get(city, 0) + 1

    averages = {}
    for city in city_totals:
        averages[city] = round(city_totals[city] / city_counts[city], 1)

    return averages


def warmest_city(records: list[dict]) -> str:
    """
    Возвращает город с наибольшей средней температурой.
    При равенстве температур возвращает первый по алфавиту.
    """
    averages = average_by_city(records)
    if not averages:
        return ""

    best_city = ""
    max_temp = float("-inf")

    # Сортируем ключи по алфавиту, чтобы при равенстве автоматически оставался первый
    for city in sorted(averages.keys()):
        if averages[city] > max_temp:
            max_temp = averages[city]
            best_city = city

    return best_city