from pyModbusTCP.client import ModbusClient
from time import sleep

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock

class ClienteMODBUS():
    """
    Classe Cliente MODBUS
    """
    def __init__(self, server_ip,porta,scan_time=1):
        """
        Construtor
        """
        self._cliente = ModbusClient(host=server_ip,port = porta)
        self._scan_time = scan_time

    def atendimento(self):
        """
        Método para atendimento do usuário
        """
        self._cliente.open()
        try:
            atendimento = True
            while atendimento:
                sel = input("Deseja realizar uma leitura, escrita ou configuração? (1- Leitura | 2- Escrita | 3- Configuração |4- Sair): ")
                
                if sel == '1':
                    tipo = input ("""Qual tipo de dado deseja ler? (1- Holding Register |2- Coil |3- Input Register |4- Discrete Input) :""")
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    nvezes = input ("Digite o número de vezes que deseja ler: ")
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo), int(addr))}")
                        sleep(self._scan_time)
                elif sel =='2':
                    tipo = input ("""Qual tipo de dado deseja escrever? (1- Holding Register) |2- Coil) :""")
                    addr = input (f"Digite o endereço da tabela MODBUS: ")
                    valor = input (f"Digite o valor que deseja escrever: ")
                    self.escreveDado(int(tipo),int(addr),int(valor))

                elif sel=='3':
                    scant = input("Digite o tempo de varredura desejado [s]: ")
                    self._scan_time = float(scant)

                elif sel =='4':
                    self._cliente.close()
                    atendimento = False
                else:
                    print("Seleção inválida")
        except Exception as e:
            print('Erro no atendimento: ',e.args)
    
    def escreveDado(self, tipo, addr, valor):
        """
        Método para a escrita de dados na Tabela MODBUS
        """
        if tipo == 1:
            return self._cliente.write_single_register(addr,valor)

        if tipo == 2:
            return self._cliente.write_single_coil(addr,valor)

class MyWidget(BoxLayout):

    def endIp(self):
        return self.root.ids.Ip.text
    
    def porta(self):
        return self.root.ids.Porta.text

    def lerDado(self, tipo):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        while self.checkbox:
            if tipo == 1:
                addr = self.ids.address.text
                return self._cliente.read_holding_registers(int(addr),1)[0]

            if tipo == 2:
                addr = self.ids.address.text
                return self._cliente.read_coils(int(addr),1)[0]

            if tipo == 1:
                addr = self.ids.address.text
                return self._cliente.read_input_registers(int(addr),1)[0]

            if tipo == 1:
                addr = self.ids.address.text
                return self._cliente.read_discrete_inputs(int(addr),1)[0]


    def checkbox(self, value):
        if value is True:
            return value
        else:
            return value

    # def endereco(self):
    #     return self.root.ids.address.text

class Aplicativo(MyWidget):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800,600)
    Window.fullscreen = False
    Aplicativo().run()

