"""
Crie uma classe Televisão e uma classe ControleRemoto que pode controlar o volume e trocar os canais de televisão.

    - O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
    - O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também possibilita
    trocar para um canal indicado;
    - Também devem existir métodos para consulta o valor do volume de som e o canal selecionado.
"""
class Television:
    
    def __init__(self, volume = 25, channel = 5):
        self.volume = volume
        self.channel = channel


class RemoteControl:

    def __init__(self):
        self.television = Television(50, 4)
        
    
    def getVolume(self):
        print(self.television.volume)
    

    def getChannel(self):
        print(self.television.channel)
    

    def turnupVolume(self):
        self.television.volume += 1
        print(f"Volume: {self.television.volume}")
    

    def turndownVolume(self):
        self.television.volume -= 1
        print(f"Volume: {self.television.volume}")
    

    def plusChannel(self):
        self.television.channel += 1
        print(f"Channel: {self.television.channel}")
    

    def minusChannel(self):
        self.television.channel -= 1
        print(f"Channel: {self.television.channel}")

    
    def selectChannel(self, new_channel):
        self.television.channel = new_channel
        print(f"Channel: {self.television.channel}")
