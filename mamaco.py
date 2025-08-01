class Macaco:
    def __init__(self, nome):
        self.nome = nome
        self.bucho = []
        
    def __str__(self):
        return f"Macaco {self.nome}" 
        
    def comer(self, comida):
        self.bucho.append(comida)
        print(f"Comida: {comida} foi comida pelo macaco {self.nome}.")
        
    def digerir(self):
        comida_permitida = ["banana", "maca", "uva", "manga", "pera"]
        for comida in self.bucho[:]:
            if isinstance(comida, Macaco):
                print(f"{self.nome} não conseguiu digerir o macaco {comida.nome}, ficou inteiro no bucho.")
                continue
            if comida in comida_permitida:
                print(f"A comida {comida} foi digerida pelo macaco {self.nome}")
            else:
                print(f"A comida {comida} não foi digerida pelo macaco {self.nome}, ele a vomitou")
            self.bucho.remove(comida)
    
    def ver_bucho(self):
        print(f"\nBucho de {self.nome}:")
        for comida in self.bucho:
            print(f" - {comida}")

        
    def comer_outro_mamaco(self, mamaco):
        if not mamaco:
            print("Este mamaco não é possível comer, pois não existe")
        self.bucho.append(mamaco)
        print("Você comeu o outro mamaco e suas comidas!")
    
macaco1 = Macaco('Bertaglia') 
macaco2 = Macaco('Enrico') 

macaco1.comer("banana")
macaco1.comer("maca")
macaco1.comer("uva")
macaco1.comer("pera")
macaco1.comer("folha")
macaco1.ver_bucho()
macaco1.digerir()
macaco2.comer("banana")
macaco2.comer("uva")
macaco2.comer("maracuja")
macaco1.comer(macaco2)
macaco1.digerir()
