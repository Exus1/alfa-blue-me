import math

dictornay = {
    "000001": "0",
    "000010": "1",
    "000011": "2",
    "000100": "3",
    "000101": "4",
    "000110": "5",
    "000111": "6",
    "001000": "7",
    "001001": "8",
    "001010": "9",
    "001011": ".",
    "001100": "A",
    "001101": "B",
    "001110": "C",
    "001111": "D",
    "010000": "E",
    "010001": "F",
    "010010": "G",
    "010011": "H",
    "010100": "I",
    "010101": "J",
    "010110": "K",
    "010111": "L",
    "011000": "M",
    "011001": "N",
    "011010": "O",
    "011011": "P",
    "011100": "Q",
    "011101": "R",
    "011110": "S",
    "011111": "T",
    "100000": "U",
    "100001": "V",
    "100010": "W",
    "100011": "X",
    "100100": "Y",
    "100101": "Z",
    "100110": "ñ",
    "100111": "ç",
    "101000": " ",
    "101001": "Ğ",
    "101010": "i",
    "101011": "j",
    "101100": "§",
    "101101": "À",
    "101110": "Ä",
    "101111": "ŭ",
    "110000": "Ü",
    "110010": "_",
    "110101": "?",
    "110110": "°",
    "110111": "!",
    "111000": "+",
    "111001": "-",
    "111010": ":",
    "111011": "/",
    "111100": "#",
    "111101": "*",
    "000000": "\r",
    "111111": "\n"
}


def __init__(self):
    pass


def decode(message: str):
    decoded = ''
    decode_index = 0
    while decode_index < len(message):

        decoded += dictornay.get(message[decode_index:decode_index + 6], '')
        decode_index += 6
    return decoded