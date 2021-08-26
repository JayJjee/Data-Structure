"""Palíndromo
Ianerisson tem uma string s com apenas letras minúsculas de 'a' a 'z'. Ele quer modificar exatamente um caractere
 por outro de 'a' a 'z' de modo que a nova string seja um palíndromo.

Um palíndromo é uma string que possui a mesma sequência de caracteres, tanto de frente para trás, como de trás 
para frente. Por exemplo as strings "z", "aaa", "aba" e "abccba" são palíndromos, enquanto as strings "unb", 
"realidade" e "ab" não são palíndromos.

Entrada
A entrada possui uma única linha com uma string s de até 100 caracteres.

Saída
Imprima "POSSÍVEL" (sem as aspas duplas) se Ianerisson puder trocar exatamente um caractere para que a string 
resultante seja um palíndromo e "IMPOSSÍVEL" (sem as aspas duplas) caso contrário.

Input	Result
abccaa  POSSÍVEL
abbcca  IMPOSSÍVEL
abcda   POSSÍVEL
 """
cont = 0
fraseNormal = input('Digite a frase: ')
fraseInvertida = fraseNormal[::-1].lower()
for cont in range(len(fraseNormal)):
    fraseAlterada = fraseInvertida
    fraseAlterada = fraseNormal.replace(fraseNormal[cont],'c')
    print(f'fraseAlterada: {fraseAlterada}')
    print(f'fraseNormal: {fraseNormal}')
    if fraseNormal[cont] == 'c':
        cont += 1
    if fraseAlterada == fraseNormal:
        print('POSSÍVEL')
    else: 
        print('IMPOSSÍVEL')
