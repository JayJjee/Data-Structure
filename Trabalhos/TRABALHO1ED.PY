bPlay = False

class Playlist:
    def __init__(self):
        self.playlist = []
        self.indice = 0
        self.buff = []

    def play(self):
        global bPlay
        if self.playlist == []:
            bPlay = False
            return bPlay
        else:
            bPlay = True
            return bPlay

    def addid(self, id):
        self.playlist.append(id)
    
    def delid(self, id):
        global bPlay
        if bPlay == True:
            if self.playlist[self.indice] == id:
                return 
            else:
                return self.playlist.remove(id)
        else:
            return self.playlist.remove(id)
    
    def nextid(self, id):
        self.indice = self.playlist.index(id)
    
    def isEmpty(self):
         return self.playlist == []

    def list(self):
        if self.isEmpty():
            print('[vazia]')
        else:
            if len(self.playlist) == 1:
                print(self.playlist[0])
            else:
                for cont in range(len(self.playlist)-1):
                    print(self.playlist[cont], end=', ') 
                print(self.playlist[cont+1])

    def current(self):
        if self.isEmpty():
            return "Toque! Toque, Dijê!"
        return self.playlist[self.indice]

    def stop(self):
        global bPlay
        bPlay = False
        return bPlay
        
    def ended(self):
        global bPlay
        if bPlay == True:
            self.indice += 1
            if self.indice >= len(self.playlist):
                self.indice = 0
        else:
            return

''' def isEmptyBuff(self):
         return self.buff == []

    def pop(self):
         return self.buff.pop()

    def push(self, item):
        self.buff.append(item)'''

listaPrincipal = Playlist()
entrada = ' '
while entrada[0] != 'fight':
    entrada = input().split()
    if entrada[0] == 'play':
        bPlay = listaPrincipal.play()
    
    elif entrada[0] == 'stop':
        bPlay = listaPrincipal.stop()

    elif entrada[0] == 'add':
        listaPrincipal.addid(entrada[1])

    elif entrada[0] == 'del':
        listaPrincipal.delid(entrada[1])

    elif entrada[0] == 'next':
        pass
 
    elif entrada[0] == 'list':
        listaPrincipal.list()
    
    elif entrada[0] == 'current':
        print(listaPrincipal.current())
    
    elif entrada[0] == 'undo':
        pass
    
    elif entrada[0] == 'ended':
        listaPrincipal.ended()

    if entrada[0] == 'fight':
        print('Jedi Wagner, assuma o comando!')