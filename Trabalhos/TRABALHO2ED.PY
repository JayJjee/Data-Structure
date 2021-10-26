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

    for code in codemsg:
        if space in code:
            mensagem.append(" ")
            mensagem.append(dic[code[1:]])
        else:
            if code in dic.values():
                mensagem.append(dic[code])
            else:
                print("Impossível decodificar a mensagem!")
                exit()
    print("".join(mensagem))

elif codemsg == 1:
    codemsg = input()
    for letter in codemsg:
        if letter == " ":
            espaço_Lista.append("/")
        else:
            if letter in dic.keys():
                espaço_Lista.append(dic[letter])
                mensagem.append(dic[letter])
                mensagem.append(" ")
            else: 
                print("Impossível codificar a mensagem!")
                exit()
    print("".join(mensagem))
