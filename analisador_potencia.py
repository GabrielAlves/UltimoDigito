from potencia_aleatoria import PotenciaAleatoria

class AnalisadorPotencia:
    def __init__(self, base, expoente):
        self.base = base
        self.expoente = expoente
        self.padrao_ultimos_digitos = self.listar_padrao_de_ultimos_digitos()
        self.ultimo_digito = self.encontrar_ultimo_digito_da_potencia()

    
    def __str__(self):
        analise = "\n"
        analise += f"Potência: {self.base}^{self.expoente}\n"
        analise += f"Base: {self.base}\n"
        analise += f"Expoente: {self.expoente}\n"
        analise += f"Último dígito: {self.ultimo_digito}\n"
        analise += f"Padrão de últimos dígitos: {self.padrao_ultimos_digitos}"
    
        return analise


    def listar_padrao_de_ultimos_digitos(self):
        ultimo_digito_numero = self.extrair_ultimo_digito_do_numero(self.base) 
        padrao_ultimos_digitos = []

        for e in range(self.expoente):      
            if ultimo_digito_numero in padrao_ultimos_digitos:
                return padrao_ultimos_digitos
                
            padrao_ultimos_digitos.append(ultimo_digito_numero)
            ultimo_digito_numero = self.calcular_ultimo_digito_do_expoente_seguinte(ultimo_digito_numero)

        # O padrão não foi encontrado. O expoente não é grande suficiente para gerar o padrão. 
        return []


    def extrair_ultimo_digito_do_numero(self, numero):
        return int(str(numero)[-1])


    def calcular_ultimo_digito_do_expoente_seguinte(self, ultimo_digito_numero):
        ultimo_digito_numero *= self.base
        ultimo_digito_numero = self.extrair_ultimo_digito_do_numero(ultimo_digito_numero)
        return ultimo_digito_numero


    def encontrar_ultimo_digito_da_potencia(self):
        padrao_ultimos_digitos = self.listar_padrao_de_ultimos_digitos()

        if padrao_ultimos_digitos:
            periodo_do_padrao = len(padrao_ultimos_digitos)
            resto_expoente = self.expoente % periodo_do_padrao

            for i in range(periodo_do_padrao):
                resto_da_posicao_do_digito_do_padrao = (i + 1) % periodo_do_padrao

                if resto_expoente == resto_da_posicao_do_digito_do_padrao:
                    ultimo_digito_potencia = padrao_ultimos_digitos[i]
                    return ultimo_digito_potencia

        # Se chegar aqui, então o expoente dado não foi grande suficiente para encontrar o padrão...
        # No entanto, isso significa que ele é pequeno o suficiente para calcular a potência e descobrir o último dígito diretamente!

        ultimo_digito_potencia = self.calcular_potencia()
        return ultimo_digito_potencia


    def calcular_potencia(self):
        potencia = pow(self.base, self.expoente)
        ultimo_digito_potencia = self.extrair_ultimo_digito_do_numero(potencia)
        return ultimo_digito_potencia


if __name__ == "__main__":
    for i in range(10):
        potencia = PotenciaAleatoria()
        analisador = AnalisadorPotencia(potencia.base, potencia.expoente)
        print(analisador)