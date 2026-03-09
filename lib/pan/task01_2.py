def panTask01_2(**kwargs):
    parts = kwargs["num"].split(',')
    total = 0
    for i in range(len(parts)):
        total += int(parts[i])
    return [
        { "color": "blue", "text": "Numbers: " },
        { "color": "black", "text": parts },
        { "color": "black", "text": "\n" },
        { "color": "blue", "text": "Sum = " },
        { "color": "blue", "text": str(total) }
    ]