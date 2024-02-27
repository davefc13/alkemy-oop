"""
Enunciado
Cierta empresa requiere una aplicación informática 
para administrar los datos de su personal, del
cual se conoce:

- número de DNI
- nombre
- apellido 
- año de ingreso.

Existen dos categorías de
empleados:-
- con salario fijo
- a comisión.

Los empleados a comisión tienen
- un salario mínimo, 
- un número de clientes captados
- un monto a cobrar por cada cliente captado.
El salario = clientes captados * monto por cliente

Si el salario obtenido por los clientes
captados no llega a cubrir el salario mínimo, cobrará
el salario mínimo. 

-----

Los empleados con salario fijo
tienen un sueldo básico y un porcentaje adicional
en función del número de años que llevan la empresa: 
• Menos de 2 años: Nada
• De 2 a 5 años: 5% más.
• Más de 5 años: 10% más.

Basado en el enunciado descripto, realizá:

A) El diagrama de clases que lo modelice, con sus relaciones, atributos y métodos.
B) La implementación del método mostrarSalarios que imprima por consola el nombre
completo de cada empleado junto a su salario.
C) La implementación del método empleadoConMasClientes que devuelva al empleado con
mayor cantidad de clientes captados (se supone único).

creen 10 empleados

"""
from enum import Enum

class CatEmpleado(Enum):
    COM = 'Por Comision'
    SAL = 'Salario Fijo'

class CatAntiguedad(Enum):
    JR = 'Menos de 2 años'
    SSR = 'De 2 a 5 años'
    SR = 'Mas de 5 años'

class Empleado():
    def __init__(
            self,
            dni: str,
            nombre: str,
            apellido: str,
            ingreso: int,
            #categoria: CatEmpleado
    ):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.ingreso = ingreso
        #self.categoria = categoria

    def MostrarSalario(self):
        pass #heredar a los hijos
        
class SalarioFijo(Empleado):
    def __init__(
            self,
            dni: str,
            nombre: str,
            apellido: str,
            ingreso: int,
            #categoria: CatEmpleado,
            sueldoBasico: float,
            #porcAdicional: float,
            antiguedad: CatAntiguedad
        ):
        super().__init__(
            dni,
            nombre,
            apellido,
            ingreso,
            #categoria
            )
        self.sueldoBasico = sueldoBasico
        #self.porcAdicional = porcAdicional
        self.antiguedad = antiguedad


    def MostrarSalario(self):
        salario = self.sueldoBasico
        if self.antiguedad == CatAntiguedad.JR.value:
            salario += self.sueldoBasico * 0/100
        elif self.antiguedad == CatAntiguedad.SSR.value:
            salario += self.sueldoBasico * 5/100
        elif self.antiguedad == CatAntiguedad.SR.value:
            salario += self.sueldoBasico * 10/100
        else:
            pass
        print('El salario de %s %s es %f' %(self.nombre, self.apellido, salario))
        return salario
        
class PorComision(Empleado):
    def __init__(
            self,
            dni: str,
            nombre: str,
            apellido: str,
            ingreso: int,
            #categoria: CatEmpleado,
            salarioMinimo: float,
            clientesCaptados: int,
            montoPorCliente: float
    ):
        super().__init__(
            dni,
            nombre,
            apellido,
            ingreso,
            #categoria
            )
        self.salarioMinimo = salarioMinimo
        self.clientesCaptados = clientesCaptados
        self.montoPorCliente = montoPorCliente
    
    def MostrarSalario(self):
        salario = self.clientesCaptados * self.montoPorCliente
        if salario < self.salarioMinimo:
            salario = self.salarioMinimo
        print('El salario de %s %s es %f' %(self.nombre, self.apellido, salario))
        return salario



empleado1 = SalarioFijo('30212344', 'Juan', 'Perez', 2017, 1200000, CatAntiguedad.SSR.value)
empleado2 = SalarioFijo('12345544', 'Luis', 'Lopez', 2022, 900000, CatAntiguedad.JR.value)
empleado3 = SalarioFijo('21357676', 'Roberto', 'Rodriguez', 2005, 1500000, CatAntiguedad.SR.value)
empleado4 = SalarioFijo('31234512', 'Ramon', 'Duran', 2023, 1200000, CatAntiguedad.JR.value)
empleado5 = SalarioFijo('14213556', 'Miguel', 'Monte', 2008, 800000, CatAntiguedad.SR.value)
empleado6 = PorComision('34343123', 'Carlos', 'Chacon', 2017, 1000000, 8, 125000)
empleado7 = PorComision('54413312', 'Carla', 'Ciro', 2017, 1000000, 2, 155000)
empleado8 = PorComision('12321556', 'Lana', 'Lane', 2017, 1000000, 1, 1155000)
empleado9 = PorComision('64234324', 'Angel', 'Lito', 2017, 1000000, 15, 118000)
empleado10 = PorComision('12312455', 'Alan', 'Brito', 2017, 1000000, 8, 155000)

nomina = [empleado1, empleado2, empleado3, empleado4, empleado5, empleado6, empleado7, empleado8, empleado9, empleado10]

for empleado in nomina:
    empleado.MostrarSalario()
