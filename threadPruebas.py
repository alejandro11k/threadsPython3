from threading import Thread, RLock

class Reloj(Thread):
    
    def __init__(self, name, count, listaCompartida):
        Thread.__init__(self)
        self.count = count
        self.name = name
        self.listaCompartida = listaCompartida
        
        
    def tick(self):
        while (self.count > 1):
            self.listaCompartida.add(self.count)
            print(self.name, self.count)
            self.count = self.count - 1
            
    def run(self):
        Thread.run(self)
        self.tick()
        
        
class ListaCompartida(Thread):
    def __init__(self):
        self.lista = []
        self.lista_lock = RLock
        
        
    def add(self, element):
        
        with self.lista_lock:
            self.lista.append(element)
            
    def printList(self):
        for x in self.lista:
            print(x)
            
    def size(self):
        return self.lista.length

class Prueba:
    
    def __init__(self, listaCompartida):
        self.listaCompartida = listaCompartida

    def run(self):
        
        r1 = Reloj("r1", 10, self.listaCompartida)
        r2 = Reloj("r2", 5, self.listaCompartida)
        r3 = Reloj("r3", 7,self.listaCompartida)
        relojes = [r1, r2, r3]
        for r in relojes:
            r.start()
            
        '''while(not self.listaCompartida.size==22):
            self.sleep(20)
        '''
            
        return self.listaCompartida
    
lc = ListaCompartida
p = Prueba(lc)
p.run()

#lc.printList()