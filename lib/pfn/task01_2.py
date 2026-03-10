def pfnTask01_2(**kwargs):
    return [
        {"color": "red", "text": ">>> "},
        {"color": "blue", "text": kwargs["ev"]},
        {"color": "blue", "text": "\n"},
        {"color": "red", "text": "    "},
        {"color": "red", "text": "???"},
    ]