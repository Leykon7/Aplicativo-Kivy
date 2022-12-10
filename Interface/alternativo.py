from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from pyModbusTCP.client import ModbusClient
from kivy.clock import Clock

class MyWidget(BoxLayout):
    i=0
    def botoes(self, tipo):
        if self.ids.repetir.active:
            if str(tipo) == '1':
                self.repetidor = Clock.schedule_interval(self.leitura1, 1)
            elif str(tipo) == '2':
                self.repetidor = Clock.schedule_interval(self.leitura2, 1)
            elif str(tipo) == '3':
                self.repetidor = Clock.schedule_interval(self.leitura3, 1)
            elif str(tipo) == '4':
                self.repetidor = Clock.schedule_interval(self.leitura4, 1)
        else:
            if str(tipo) == '1':
                self.leitura1(0)
            elif str(tipo) == '2':
                self.leitura2(0)
            elif str(tipo) == '3':
                self.leitura3(0)
            elif str(tipo) == '4':
                self.leitura4(0)

    def leitura1 (self, dt):
        addr = self.ids.address.text
        if self.ids.repetir.active:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_holding_registers(int(addr),1)[0])
            self.ids.foi_lido.text = lido
        else:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_holding_registers(int(addr),1)[0])
            self.ids.foi_lido.text = lido
            self.repetidor.cancel()
        self.i+=1

    def leitura2 (self, dt):
        addr = self.ids.address.text
        if self.ids.repetir.active:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_coils(int(addr),1)[0])
            self.ids.foi_lido.text = lido
        else:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_coils(int(addr),1)[0])
            self.ids.foi_lido.text = lido
            self.repetidor.cancel()

    def leitura3 (self, dt):
        addr = self.ids.address.text
        if self.ids.repetir.active:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_input_registers(int(addr),1)[0])
            self.ids.foi_lido.text = lido
        else:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_input_registers(int(addr),1)[0])
            self.ids.foi_lido.text = lido
            self.repetidor.cancel()
            
    def leitura4 (self, dt):
        addr = self.ids.address.text
        if self.ids.repetir.active:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_discrete_inputs(int(addr),1)[0])
            self.ids.foi_lido.text = lido
        else:
            lido = f'Leitura {self.i}: ' + str(self._cliente.read_discrete_inputs(int(addr),1)[0])
            self.ids.foi_lido.text = lido
            self.repetidor.cancel()
    
    # def parar(self):
    #     return self.repetidor.cancel()

    def conectar(self):
        try:
            self._cliente = ModbusClient(host=self.ids.Ip.text, port = int(self.ids.Porta.text))
            self._scan_time = 1

            self._cliente.open()
            self.ids.conectar.text = 'Desconectar'
            self.ids.foi_lido.text = """Digite o endereço 
e selecione o tipo de leitura"""

        except Exception as e:
            self.ids.conectar.text = 'Conectar'
            print('Erro no atendimento: ',e.args)

class AplicativoAlternativo(App):

    def build(self):
        return MyWidget()

if __name__ == '__main__':
    Window.size = (800,600)
    Window.fullscreen = False
    AplicativoAlternativo().run()