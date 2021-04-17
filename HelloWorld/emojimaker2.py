def text2emoji(message):
    emojis = {
        ":)": "😀",
        ";)": "( ͡° ͜ʖ ͡°)",
        "=)": "😃",
        "xD": "😆",
        "XD": "🤣",
        ":D": "😁",
        "=D": "😁",
        ":p": "😋",
        ":P": "😛",
        "xP": "😝",
        ";P": "😜",
        ":o": "😯",
        ":O": "😦",
        ":0": "😧",
        ":(": "😟",
        ":middle_finger:": "🖕",
        ":eggplant:": "🍆"
    }
    text = ''
    words = message.split(' ')
    for word in words:
        text += emojis.get(word, word) + " "
    return text


while True:
    print(text2emoji(input(">")))