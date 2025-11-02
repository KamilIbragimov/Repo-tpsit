from veicolo import Veicolo

class Auto(Veicolo):
    def __init__(self, marca, modello, porte):
        super().__init__(marca, modello)
        self.porte = porte

   