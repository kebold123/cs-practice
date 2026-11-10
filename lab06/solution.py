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

def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
    
    max_depth = -1
    result = ""
    
    for path in paths:
        depth = path.count("/")
        
        if depth > max_depth or (depth == max_depth and path < result):
            max_depth = depth
            result = path
    
    return result