def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        filename = path.split("/")[-1]  # берём имя файла
        
        if "." in filename:
            ext = filename.rsplit(".", 1)[1].lower()  # всё после последней точки
        else:
            ext = ""
        
        counts[ext] = counts.get(ext, 0) + 1
    
    return counts