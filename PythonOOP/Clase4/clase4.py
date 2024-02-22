class Auto():
    #Constructor, definir atributos
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    #metodos
    #getters
    def getMarca(self):
        return self.marca
    def getModelo(self):
        return self.modelo
    def getColor(self):
        return self.color
    
auto1 = Auto('Ford', 'Fiesta', 'Blanco')
print(auto1.modelo)
print(auto1.getModelo())