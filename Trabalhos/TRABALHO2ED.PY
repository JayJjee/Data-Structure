def insert(self, elem):
        
        if len(elem[1]) == self.altura:
            self.chave = elem[0]
        elif len(elem[1])> self.altura:
            ta  = Arvore(self.altura+1)
            if elem[1][self.altura] == '.':
                if not self.esq: self.esq = ta
                else: ta=self.esq
            else:
                if not self.dir: self.dir = ta
                else: ta=self.dir
                
            ta.insert(elem)