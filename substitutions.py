code = input("enter code: ")
wtd = input("encode or decode: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
key = "qwertyuiopasdfghjklzxcvbnm"
def encode(code):
    solution = ""
    for i in code:
        for j in alphabet:
            if i == j:
                solution += key [alphabet.index(j)]

    return solution
def decode(code):
    solution = ""
    for i in code:
        for j in key:
            if i == j:
                solution += alphabet[key.index(j)]
    return solution
if wtd == "encode":
    print(encode(code))
if wtd == "decode":
    print(decode(code))
