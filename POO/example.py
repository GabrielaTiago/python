# Desadio 1:

# Crie uma classe abstrata chamada Monitor, que irá ter 2 métodos abstratos: aumentar_claridade e reduzir_claridade.
# Os métodos irão receber um número que representam o quanto de claridade deve ser aumentado ou diminuído ao chamá-los.
# Após ter criado a classe abstrata, crie um nova classe chamada de MonitorFullHD e coloque a implementação dos métodos aumentar_claridade e reduzir claridade dentro deles.

from abc import ABC, abstractmethod

class Monitor(ABC):
    @abstractmethod
    def aumentar_claridade(self, valor):
        pass

    @abstractmethod
    def reduzir_claridade(self, valor):
        pass

class MonitorFullHD(Monitor):
    luminosidade = 50

    def aumentar_claridade(self, valor):
        self.luminosidade += valor
        print(f'Aumentando a claridade em {valor}')

    def reduzir_claridade(self, valor):
        self.luminosidade -= valor
        print(f'Reduzindo a claridade em {valor}')

    def claridade_atual(self):
        print(f'A claridade atual é de {self.luminosidade}')

monitor = MonitorFullHD()
monitor.aumentar_claridade(10) # Aumentando a claridade em 10
monitor.claridade_atual() # A claridade atual é de 60
monitor.reduzir_claridade(5) # Reduzindo a claridade em 5
monitor.claridade_atual() # A claridade atual é de 55

