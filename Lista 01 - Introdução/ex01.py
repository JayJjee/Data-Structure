def divisores(n):

    numerosDivisores = [] #Cria a lista
    
    for contador in range(2, n + 1): #O contador no invervalo de tempo de 1 até n+1, faz:
        if n % contador == 0: #Se a divisão entre o numero solicitado e o contador for igual a 0
            numerosDivisores.append(contador) #A lista criada recebe o contador que basicamente são os divisores
    
    return numerosDivisores #Retorna a lista com os números

print(divisores(10)) #Exemplo

