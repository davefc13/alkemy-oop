class  Bicicleta:
    def __init__(
            self,
            marca,
            modelo,
            color,
            rodado,
            cambios,
            precio,
            velocidad
    ):
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.rodado = rodado
        self.cambios = cambios
        self.precio = precio
        self.velocidad = velocidad
    
    def mostrarBici(self):
        print('----------------')
        print('marca: %s' %self.marca)
        print('modelo: %s' %self.modelo)
        print('color: %s' %self.color)
        print('rodado: %i' %self.rodado)
        print('cambios: %i' %self.cambios)
        print('precio: %i' %self.precio)
        print('velocidad: %i' %self.velocidad)

    def actualizarPrecio(self, porcentaje):
        print('Precio actual: %i' %self.precio)
        self.precio *= (1 + porcentaje/100)
        print('Precio nuevo: %i' %self.precio)

    def ajustarCambios(self, cambio):
        print('Velocidad actual: %i' %self.velocidad)
        if (self.velocidad > 1) and (self.velocidad < self.cambios):
            self.velocidad += cambio
        print('Velocidad nueva: %i' %self.velocidad)

miBici = Bicicleta('Shimano', 'RTX', 'Rosa', 26, 21, 750000, 15)

miBici.mostrarBici()

miBici.actualizarPrecio(25)

miBici.ajustarCambios(1)
miBici.ajustarCambios(1)

for i in range(1,20):
    miBici.ajustarCambios(-1)