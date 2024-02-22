from enum import Enum

class Vertebra(Enum):
    VER = 'Vertebrado'
    INV = 'Invertebrado'

class CantPata(Enum):
    UNA = 1
    DOS = 2
    TRES = 3
    CUAT = 4

class Raza(Enum):
    GOLD = 'Golden Retriever'
    CANI = 'Caniche'
    PITB = 'Pitbull'
    BEAG = 'Beagle'

class Animal():
    def __init__(
            self,
            cantidad_patas,
            tipo
    ):
        self.cantidad_patas = cantidad_patas
        self.tipo = tipo

    def comer(self):
        print('Estoy comiendo nom nom')

class Perro(Animal):
    def __init__(
            self,
            cantidad_patas,
            tipo,
            nombre,
            raza
    ):
        super().__init__(
            cantidad_patas,
            tipo
        )
        self.nombre = nombre
        self.raza = raza

    def correr(self):
        print('Soy %s, un %s y tengo %i patas - estoy corriendo guau guau!!' %(self.nombre, self.raza, self.cantidad_patas))

class Aguila(Animal):
    def __init__(
            self,
            cantidad_patas,
            tipo
    ):
        super().__init__(
            cantidad_patas,
            tipo
        )

    def volar(self):
        print('Soy un aguila %s y tengo %i patas - y estoy volando fiuuu' %(self.tipo, self.cantidad_patas))


miPerro = Perro(CantPata.CUAT.value, Vertebra.VER.value, 'Rocco', Raza.BEAG.value)
miPerro.correr()
miPerro.comer()

pajaro = Aguila(CantPata.UNA.value, Vertebra.INV.value)
pajaro.volar()
pajaro.comer()
