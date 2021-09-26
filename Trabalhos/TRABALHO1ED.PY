bPlay = False
actionList = []
deleted = []

class Playlist:
    def __init__(self):
        self.playlist = []
        self.indice = 0
        self.buff = []

    def isEmpty(self):
         return self.playlist == []

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
        if self.isEmpty():
            pass
        else:
            if bPlay == True:
                if self.playlist[self.indice] == id:
                    return 0
                else:
                    deleted.append(id)
                    return self.playlist.remove(id)
            else:
                deleted.append(id)
                return self.playlist.remove(id)
    
    def nextid(self, id):
        global bPlay
        if self.isEmpty():
            pass
        else:
            if bPlay == True:
                for cont in range(len(self.playlist)):
                    if id == self.playlist[cont] and id != self.playlist[self.indice]:
                        self.playlist.remove(id)
                        self.playlist.insert(self.indice+1, id)

            else:
                for cont in range(len(self.playlist)):
                    if id == self.playlist[cont] and id != self.playlist[self.indice]:
                        self.playlist.remove(id)
                        self.playlist.insert(self.indice, id)

    def list(self):
        if self.isEmpty():
            print('[vazia]')
        else:
            if len(self.playlist) == 1:
                print(self.playlist[0])
            else:
                for cont in range(len(self.playlist)-1):
                    print(self.playlist[cont], end=',')
                print(self.playlist[cont+1])

    def current(self):
        if self.isEmpty():
            return print("Toque! Toque, Dijê!")
        elif len(self.playlist) == 1:
            print(self.playlist[0])
        else:
            print(self.playlist[self.indice])

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
    def undo(self):        
        if self.isEmpty():
            pass
        else:
            global bPlay
            contList = len(self.playlist)-1
            for acao in actionList[::-1]:
                if acao == 'add':
                    return self.playlist.remove(self.playlist[contList]) 
                elif acao == 'del':
                    pass
                elif acao == 'next':
                    pass
                elif acao == 'play':
                    bPlay = False
                    return bPlay
                contList -= 1
    def undoast(self):
        global bPlay
        contList = len(self.playlist)-1
        for acao in actionList[::-1]:
            if acao == 'add':
                self.playlist.remove(self.playlist[contList])
                contList -= 1
            elif acao == 'del':
                self.playlist.append(self.playlist[contList])
                contList -= 1
            elif acao == 'next':
                contList -= 1
            elif acao == 'play':
                bPlay = False
                contList -= 1

listaPrincipal = Playlist()
entrada = ' '
while entrada[0] != 'fight':
    entrada = input().split()

    if entrada[0] == 'play':
        bPlay = listaPrincipal.play()
        actionList.append('play')

    elif entrada[0] == 'stop':
        bPlay = listaPrincipal.stop()
    
    elif entrada[0] == 'add':
        listaPrincipal.addid(entrada[1])
        actionList.append('add')

    elif entrada[0] == 'del':
        listaPrincipal.delid(entrada[1])
        actionList.append('del')

    elif entrada[0] == 'next':
        listaPrincipal.nextid(entrada[1])
        actionList.append('next')
 
    elif entrada[0] == 'list':
        listaPrincipal.list()
    
    elif entrada[0] == 'current':
        listaPrincipal.current()

    elif entrada[0] == 'undo':
        listaPrincipal.undo()

    elif entrada[0] == 'undo':
        if len(entrada) > 1:
            if entrada[1] == '*':
                listaPrincipal.undoast()

    elif entrada[0] == 'ended':
        listaPrincipal.ended()

    if entrada[0] == 'fight':
        print('Jedi Wagner, assuma o comando!')