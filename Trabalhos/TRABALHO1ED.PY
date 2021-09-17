class Playlist:
    def __init__(self):
        self.playlist = []
        self.indice = 0
        self.buff = []

    def play(self):
        if self.playlist == []:
            return False
        else:
            self.indice += 1
            if self.indice == len(self.playlist):
                self.indice = 0
            return True

    def addid(self, item):
        self.playlist.append(item)
    
    def delid(self, pos):
        return self.playlist.remove(pos)
    
    def nextid(self, id):
        self.indice = self.playlist.index(id)
    
    def list(self):
        if self.isEmpty():
            print('[vazia]')
        else:
            for cont in range(len(self.playlist)):
                print(self.playlist[cont], end=', ')
            print(self.playlist[cont+1])

    def current(self):
        if self.isEmpty():
            return "Toque! Toque, Dijê!"
        return self.playlist[self.indice]
    
    def isEmpty(self):
         return self.playlist == []

    def isEmptyBuff(self):
         return self.buff == []

    def pop(self):
         return self.buff.pop()

    def push(self, item):
        self.buff.append(item)

    '''def undo()#pra cada ação uma reconstrução'''

entrada = input().split()
listaPrincipal = Playlist()

while entrada[0] != 'fight':
    if entrada[0] == 'play':
        pass

    elif entrada[0] == 'stop':
        pass

    elif entrada[0] == 'add':
        listaPrincipal.addid(entrada[1])

    elif entrada[0] == 'del':
        listaPrincipal.delid(entrada[1])

    elif entrada[0] == 'next':
        pass

    elif entrada[0] == 'list':
        pass
    elif entrada[0] == 'current':
        print(listaPrincipal.current())
    elif entrada[0] == 'undo':
        pass
    elif entrada[0] == 'ended':
        pass