root = " "

class Arvore:

    def __init__(self, higher):

        self.left = None
        self.right = None
        self.higher = higher
        self.key = "*"
        
    def __str__(self):

        return '%s' %(self.key) 

    def height(self, node = root):

        if node == root:
            node = self.key

        list = []
        list.insert(0, node)

        while list != []:
            node = list.pop()
            print(node, end = " ")

            if node.left:
                list.insert(0, node.left)
            if node.right:
                list.insert(0, node.right)

    def insert(self, elem):

        if len(elem[1]) == self.higher:
            self.key = elem[0]

        elif len(elem[1])> self.higher:
            TREE = Arvore(self.higher+1)

            if elem[1][self.higher] == '.':
                if not self.left: 
                    self.left = TREE
                else: TREE=self.left
            else:
                if not self.right: 
                    self.right = TREE
                else: TREE=self.right
                
            TREE.insert(elem)

def get_key(val):

    for chave, valor in dic.items():
         if val == valor:
             return chave

numberInput = int(input())
dic = {}
mensagem = []
espaço_Lista = []
myTree = Arvore(0)

for cont in range(numberInput):
    morse = input().split()
    letter = morse[0]
    code = morse[1]
    dic.update({letter:code})
    myTree.insert(morse)

n = int(input())

if n == 0:
    codemsg = input().split()
    space = "/"
    bMes = True

    for code in codemsg:
        if code in dic.values():
            mensagem.append(get_key(code))

        elif space in code:
            mensagem.append(" ")

            if get_key(code[1:]) == None:
                pass
            else:
                mensagem.append(get_key(code[1:]))

        else:
            bMes = False

    if bMes == True:
        print("".join(mensagem))
        myTree.height(myTree)
    else:
        print("Impossível codificar a mensagem!")

elif n == 1:
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
        myTree.height(myTree)
    else:
        print("Impossível codificar a mensagem!")