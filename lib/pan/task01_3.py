def panTask01_3(**kwargs):
    def center_text(text: str, length: int = 31) -> str:
        if len(text) >= length:
            return text
        total_padding = length - len(text)
        left_padding = total_padding // 2
        right_padding = total_padding - left_padding
        return " " * left_padding + text + " " * right_padding

    def left_text(text: str, length: int = 15) -> str:
        if len(text) >= length:
            return text
        return text.ljust(length, " ")

    def right_text(text: str, length: int = 15) -> str:
        if len(text) >= length:
            return text
        return text.rjust(length, " ")

    # Split the incoming strings into [name, height]
    parts1 = (kwargs["p1"] or "").split()
    parts2 = (kwargs["p2"] or "").split()

    return [
        {"color": "blue", "text": "Person 1 | Name and Height: "},
        {"color": "black", "text": parts1},
        {"color": "black", "text": "\n"},
        {"color": "blue", "text": "Person 2 | Name and Height: "},
        {"color": "black", "text": parts2},
        {"color": "black", "text": "\n"},
        {"color": "blue", "text": center_text("List")},
        {"color": "black", "text": "\n"},
        {"color": "blue", "text": "=" * 31},
        {"color": "black", "text": "\n"},
        {
            "color": "blue",
            "text": f"{left_text(parts1[0])}|{right_text(parts1[1] if len(parts1) > 1 else '')}",
        },
        {"color": "black", "text": "\n"},
        {
            "color": "blue",
            "text": f"{left_text(parts2[0])}|{right_text(parts2[1] if len(parts2) > 1 else '')}",
        },
        {"color": "black", "text": "\n"},
        {"color": "blue", "text": "=" * 31},
    ]
