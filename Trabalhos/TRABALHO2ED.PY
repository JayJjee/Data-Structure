def get_key(val):
    for chave, valor in dic.items():
         if val == valor:
             return chave

numberInput = int(input())
dic = {}
mensagem = []
espaço_Lista = []

for cont in range(numberInput):
    morse = input().split()
    letter = morse[0]
    code = morse[1]
    dic.update({letter:code})

codemsg = int(input())

if codemsg == 0:
    codemsg = input().split()
    space = "/"
    bMes = True

    for code in codemsg:
        if code in dic.values():
            mensagem.append(get_key(code))
        elif space in code:
            mensagem.append(" ")
            if get_key(code) == None:
                pass
            else:
                mensagem.append(get_key(code[1:]))
        else:
            bMes = False
    if bMes == True:
        print(mensagem)
        print("".join(mensagem))
    else:
        print("Impossível codificar a mensagem!")

elif codemsg == 1:
    codemsg = input()
    bMes = True
    for letter in codemsg:
        if letter in dic.keys():
            espaço_Lista.append(dic[letter])
            mensagem.append(dic[letter])
            mensagem.append(" ")
        elif letter == " ":
            mensagem.append("/")
            if mensagem[-2] == "/":
                mensagem.pop()
        else:
            bMes = False
    if bMes == True:
        print("".join(mensagem))
    else:
        print("Impossível codificar a mensagem!")