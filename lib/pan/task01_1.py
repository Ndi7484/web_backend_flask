def panTask01_1(**kwargs):
    parts = kwargs['num'].split()
    radius = float(parts[0]) if len(parts) > 0 else 0
    height = float(parts[1]) if len(parts) > 1 else 0
    pi = 3.14
    formatted = round(pi*radius*radius*height,2)
    return[
        { "color": "blue", "text": "Numbers: " },
        { "color": "black", "text": f"{radius} {height}" },
        { "color": "black", "text": "\n" },
        { "color": "blue", "text": "Volume = " },
        { "color": "blue", "text": formatted }
    ]