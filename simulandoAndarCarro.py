class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        
    def __str__(self):
        return f"Marca: {self.marca} | Modelo: {self.modelo}"
    
class Carro(Veiculo):
    def __init__(self, marca, modelo, kmLitros):
        super().__init__(marca, modelo)
        self.km_litros = kmLitros
        self.qt_combustivel = 0
        self.combustivelAtual = self.qt_combustivel
        self.capacidade_tanque = 50
        print("Veículo criado com sucesso!")
    
    def __str__(self):
        return f"{super().__str__()} | Km/p litro: {self.km_litros}"
    
    def abastecer(self, litros):
        espaco_disponivel = self.capacidade_tanque - self.qt_combustivel
        if espaco_disponivel <= 0:
            print("Não foi possível abastecer, o tanque já está cheio!")
            return

        litros_abastecidos = min(litros, espaco_disponivel)
        self.qt_combustivel += litros_abastecidos
        print(f"Combustível abastecido: {litros_abastecidos} litro(s)")
        self.atualizar_km()
        
    def andar(self, distancia):
        if self.qt_combustivel == 0:
            print("Não há combustível para andar! Abasteça o tanque.")
            return
        litros_necessarios = distancia / self.km_litros

        if litros_necessarios > self.qt_combustivel:
            distancia_possivel = self.qt_combustivel * self.km_litros
            print(f"Você não tem combustível suficiente para andar {distancia}Km.")
            print(f"Andando {distancia_possivel:.2f}Km com o combustível restante.")
            self.qt_combustivel = 0
        else:
            self.qt_combustivel -= litros_necessarios
            print(f"Você andou {distancia}Km, gastando {litros_necessarios:.2f} litros.")
            print(f"Combustível restante: {self.qt_combustivel:.2f} litros.")

        self.atualizar_km()

    def atualizar_km(self):
        self.combustivelAtual = self.qt_combustivel
        
    def saber_gas(self):
        print(f"Tanque de gasolina: {self.qt_combustivel:.2f} litro(s)")
        
carro = Carro("VolksWagem", "Gol", 12)
carro.saber_gas()        
carro.andar(14)
carro.abastecer(30)
carro.saber_gas()
carro.abastecer(21)
carro.andar(20)
