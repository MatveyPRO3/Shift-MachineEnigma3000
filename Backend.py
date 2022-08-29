import random as r
import sys
import string


def one_time_pad_cypher(message):
    essage = list(message)
    key = [r.randint(0, 26) for x in range(len(message))]
    ASCII = list(string.printable)[:-10]
    l = []
    for i, j in enumerate(message):
        l.append(ASCII[ord(j)+key[i]] if ord(j)+key[i] <
                 len(ASCII) else ASCII[ord(j)+key[i]-len(ASCII)])
    return "Message:", "".join(l), "KEY:", key


def cesars_cypher(message, num):
    alphabet = list(string.printable)[:-10]
    code_word = []
    word = message
    num = int(num)
    for i in word:
        code_word.append(
            alphabet[alphabet.index(i)+num-90] if i != " " else " ")
    return "Coded word: ", "".join(code_word)


def XOR_cypher(text, func="code", key=None):
    def help_function(message):  # making simple number from binarry code
        b_num = message
        value = 0
        for i in range(len(b_num)):
            digit = b_num.pop()
            if digit == '1':
                value = value + pow(2, i)
        return value

    def generate_binary_key():
        key = []
        for x in range(8):
            a = r.randint(0, 1)
            key.append(a)
        return key
    if func == "decode":
        word = text
        binary_w = [bin(ord(x))[2:].zfill(8) for x in word]
        text = list(word)
    elif func == "code":
        key = "".join(map(str, generate_binary_key()))
        text = str(text)
    a_list = []
    shift_message = []
    deshift_message = []
    text = list(text)
    for i in text:
        letter = ord(i)  # creating simple number
        # creating binnary code of simple number
        shift_letter = list(bin(letter).replace("0b", "").zfill(8))
        a_list = []
        for j in range(0, len(key)):
            if key[j] == shift_letter[j]:
                a_list.append("0")
            else:
                a_list.append("1")
        shift_message.append(a_list)
    letter = 0
    for x in shift_message:
        letter = help_function(x)
        if func == "code":
            for _ in ("inf"):
                if letter < 26:
                    letter += 26
                elif letter > 126:
                    letter -= 126
                else:
                    break
        letter = chr(letter)
        deshift_message.append(letter)
    return "message:", "".join(deshift_message), "KEY:", "".join(key)


def decoding_for_one_time_pad_cypher(message, key):
    # message = list(message)
    # key = key.split(" ")
    # l=list()
    # ASCII = list(string.printable)[:-6]
    # for i in range(message):
    #     pass
    return "Message:", "".join("message")


def decoding_for_cesars_cypher():
    return "oops. Sorry, but this doesn't work."
