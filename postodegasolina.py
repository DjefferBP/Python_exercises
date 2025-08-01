class Funcionario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
    def __str__(self):
        return f"Funcionário {self.nome} com {self.idade} anos."

class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade        
        
    def __str__(self):
        return f"Cliente {self.nome} com {self.idade} anos."
    

class Posto:
    def __init__(self):
        self.combustiveis = [
            {"tipo": "Gasolina", "qt": 5000, "valor": 4.79},
            {"tipo": "Etanol", "qt": 5000, "valor": 5.5},
            {"tipo": "Álcool", "qt": 5000, "valor":5.3}
        ]
        
    def abastecer_por_valor(self,cliente, tipoCombs, valor):
        tipo = next((u for u in self.combustiveis if u["tipo"] == tipoCombs), None)
        if tipo == None:
            print("Não encontrado. Escolha entre as opções: Gasolina, Etanol ou Álcool")
            return
        vlgas = tipo["valor"]
        quantidade = valor / vlgas
        qtLitro = tipo["qt"]
        if qtLitro < quantidade:
            print("Não temos combustível suficiente para reabastecer.")
            return
        print(f"Valor do(a) {tipo["tipo"]}: R${tipo["valor"]}")
        print(f"Valor abastecido: R${valor} - Tipo do combustível: {tipoCombs} - Quantidade de combustível abastecida: {quantidade:.2f}")
        print("Cliente:", cliente.nome, "abasteceu com sucesso!")
        self.alterar_quantidade_combustivel(tipoCombs, quantidade)
        
    def alterar_quantidade_combustivel(self,tipoCombus, qt):
        tipo = next((u for u in self.combustiveis if u["tipo"] == tipoCombus), None)
        if tipo == None:
            print("Não encontrado.")
            return
        tq = tipo["qt"] - qt
        tipo["qt"] = tq
        
    def abastecer_por_litro(self,cliente, tipoCombs, litros):
        tipo = next((u for u in self.combustiveis if u["tipo"] == tipoCombs), None)
        if tipo == None:
            print("Não encontrado. Escolha entre as opções: Gasolina, Etanol ou Álcool")
            return
        qtLitro = tipo["qt"]
        vlgas = tipo["valor"]
        if qtLitro < litros:
            print("Não temos combustível suficiente para reabastecer.")
            return
        print(f"Valor do(a) {tipo["tipo"]}: R${tipo["valor"]}")
        pagar = vlgas * litros
        print(f"Quantidade de combustível abastecida: {litros} - Tipo do combustível: {tipoCombs} - Valor a ser pago: R${pagar:.2f}")
        print("Cliente:", cliente.nome, "abasteceu com sucesso!")
        self.alterar_quantidade_combustivel(tipoCombs, litros)
        
    def alterar_valor(self,tipo, valor):
        tipo = next((u for u in self.combustiveis if u["tipo"] == tipo), None)
        if tipo == None:
            print("Não encontrado. Escolha entre as opções: Gasolina, Etanol ou Álcool")
            return
        tipo["valor"] = valor
        print(f"Valor do combustível {tipo["tipo"]} alterado para R${tipo["valor"]}\n")
        
        
    def ver_quantidade_combustivel(self):
        for c in self.combustiveis:
            print(f"Combustível: {c['tipo']} - Quantidade de Combustível: {c['qt']:.2f}L - Valor: R${c['valor']}")

    
    
func = Funcionario("Alessandro", 54)
c1 = Cliente("Gilmar", 32)
posto = Posto()
posto.alterar_valor("Gasolina", 6.10)
posto.abastecer_por_valor(c1, "Álcool", 50)
posto.abastecer_por_litro(c1, "Etanol", 32)
posto.abastecer_por_litro(c1, "Gasolina", 50)
posto.abastecer_por_valor(func, "Gasolina", 150)
