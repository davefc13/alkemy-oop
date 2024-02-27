from enum import Enum

class Profesion(Enum):
    ABG = 'Abogado'
    ING = 'Ingeniero'
    MED = 'Medico'

class ColorBici(Enum):
    AMA = 'Amarillo'
    ROJ = 'Rojo'
    AZU = 'Azul'

class MarcaBici(Enum):
    SHI = 'Shimano'
    MAS = 'Massino'
    PIR = 'Pirula'


class Persona():
    def __init__(
            self,
            nombre,
            apellido,
            edad,
            profesion,
    ):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.profesion = profesion

class Bicicleta():
    def __init__(
            self,
            marca,
            color
    ):
        self.marca = marca
        self.color = color

class Paseos(Persona):
    def __init__(
        self,
        nombre,
        apellido,
        edad,
        profesion,
        marca,
        color
    ):
        super().__init__(
            nombre,
            apellido,
            edad,
            profesion,
            marca,
            color
        )
    
    def aPie(self):
        print('En la tarde, despues de su laburo como %s, %s sale a caminar.' %(self.profesion, self.nombre))

    def enBici(self):
        print('A veces, %s sale a dar vueltas en su bicicleta %s marca %s.' %(self.nombre, self.color, self.marca))





juan = Persona('Juan', 'Lopez', 25, Profesion.ABG.value, MarcaBici.MAS.value, ColorBici.AMA.value)
juan.aPie()
juan.enBici()
