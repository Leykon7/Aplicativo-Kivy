from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from pyModbusTCP.client import ModbusClient
from time import sleep
import threading
from kivy.clock import Clock

def Repeticao(self, tipo, addr):

    self.ids.repetir.text = 'Parar leitura contínua'
    i=1
    while self.ids.repetir.active:
        
        if tipo == 1:
            self.ids.foi_lido.text = f'Leitura {i}: '+ str(self._cliente.read_holding_registers(int(addr),1)[0])
            print(f'Leitura {i}: '+ str(self._cliente.read_holding_registers(int(addr),1)[0]))

        elif tipo == 2:
            self.ids.foi_lido.text = f'Leitura {i}: '+ str(self._cliente.read_coils(int(addr),1)[0])

        elif tipo == 3:
            self.ids.foi_lido.text = f'Leitura {i}: '+ str(self._cliente.read_input_registers(int(addr),1)[0])

        elif tipo == 4:
            self.ids.foi_lido.text = f'Leitura {i}: '+ str(self._cliente.read_discrete_inputs(int(addr),1)[0])
        sleep(1)
        i=i+1
        self.ids.foi_lido.text

class MyWidget(BoxLayout):

    def conectar(self):
        try:
            self._cliente = ModbusClient(host=self.ids.Ip.text, port = int(self.ids.Porta.text))
            self._scan_time = 1

            self._cliente.open()
            self.ids.conectar.text = 'Desconectar'
            self.ids.foi_lido.text = 'Digite o endereço e selecione o tipo de leitura'

        except Exception as e:
            self.ids.conectar.text = 'Conectar'
            print('Erro no atendimento: ',e.args)


    def lerDado(self, tipo):

        addr = self.ids.address.text
        if self.ids.repetir.active:
            linha = threading.Thread(target=Repeticao, args=(self, tipo, addr))
            linha.start()
        else:
            if tipo == 1:
                lido = str(self._cliente.read_holding_registers(int(addr),1)[0])
                
            elif tipo == 2:
                lido = str(self._cliente.read_coils(int(addr),1)[0])

            elif tipo == 3:
                lido = str(self._cliente.read_input_registers(int(addr),1)[0])

            elif tipo == 4:
                lido = str(self._cliente.read_discrete_inputs(int(addr),1)[0])
            self.ids.foi_lido.text = lido

class Aplicativo(App):

    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800,600)
    Window.fullscreen = False
    Aplicativo().run()

