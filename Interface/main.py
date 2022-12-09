from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.clock import Clock
from pyModbusTCP.client import ModbusClient
from time import sleep

class MyWidget(BoxLayout):
    
    def conectar(self):
        try:
            self._cliente = ModbusClient(host=self.ids.Ip.text ,port = int(self.ids.Porta.text))
            self._scan_time = 1

            self._cliente.open()
            
            self.ids.leitura.text = 'Selecione o tipo de leitura'

        except Exception as e:
            print('Erro no atendimento: ',e.args)


    def lerDado(self, tipo):
        """
        Método para leitura de um dado da Tabela MODBUS
        """
        if self.ids.repetir.active:
            i=0
            addr = self.ids.address.text
            if tipo == 1:
                while self.ids.repetir.active:
                    i+=1
                    self.ids.leitura.text = f'Leitura {i}: '+ str(self._cliente.read_holding_registers(int(addr),1)[0])

            if tipo == 2:
                while self.ids.repetir.active:
                    i+=1
                    self.ids.leitura.text = f'Leitura {i}: '+ str(self._cliente.read_coils(int(addr),1)[0])

            if tipo == 1:
                while self.ids.repetir.active:
                    i+=1
                    self.ids.leitura.text = f'Leitura {i}: '+ str(self._cliente.read_input_registers(int(addr),1)[0])

            if tipo == 1:
                while self.ids.repetir.active:
                    i+=1
                    self.ids.leitura.text = f'Leitura {i}: '+ str(self._cliente.read_discrete_inputs(int(addr),1)[0])
                sleep(5)
        else:
            if tipo == 1:
                addr = self.ids.address.text
                self.ids.leitura.text = str(self._cliente.read_holding_registers(int(addr),1)[0])

            if tipo == 2:
                addr = self.ids.address.text
                self.ids.leitura.text = str(self._cliente.read_coils(int(addr),1)[0])

            if tipo == 1:
                addr = self.ids.address.text
                self.ids.leitura.text = str(self._cliente.read_input_registers(int(addr),1)[0])

            if tipo == 1:
                addr = self.ids.address.text
                self.ids.leitura.text = str(self._cliente.read_discrete_inputs(int(addr),1)[0])


class Aplicativo(App):
    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800,600)
    Window.fullscreen = False
    Aplicativo().run()
