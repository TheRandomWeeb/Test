while True:
    message = input(">")


    def text2emoji(text):
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
        words = text.split(' ')
        for word in words:
            text += emojis.get(word, word) + " "
        return


    print(message)