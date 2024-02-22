""" class Persona:
    def __init__(self, nombre, apellido):
        self.__nombre = nombre
        self.apellido = apellido
    
    def mostrarnombre(self):
        print(self.__nombre)

    def cambiarnombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
        print('Nuevo nombre es: %s' %self.__nombre)

persona = Persona('Juan', 'Perez')
#print(persona.__nombre)
print(persona.apellido)

persona.mostrarnombre()
persona.cambiarnombre('Roberto')

persona.apellido = 'Lopez'
print(persona.apellido)

persona.__nombre = 'Lopez'
persona.mostrarnombre() """

from enum import Enum

# genero cine
# genero musico
# genero libro
# clasificacion cine
# formato musica

class GeneroCine(Enum):
    TERR = 'Terror'
    COME = 'Comedia'
    INFA = 'Infantil'

class GeneroMusica(Enum):
    CLAS = 'Clasica'
    FOLK = 'Folkore'
    ROCK = 'Rock'
    TROP = 'Tropical'

class GeneroLibro(Enum):
    NOVE = 'Novela'
    CIEN = 'Ciencia Ficcion'
    RECE = 'Recetario'
    MANG = 'Manga'

class ClasificacionCine(Enum):
    ATP = 'Apto Todo Publico'
    MAS18 = '+18'
    MAS16 = '+16'

class FormatoMusica(Enum):
    CD = 'Compact Disk'
    VINIL = 'Disco Vinilo'
    KST = 'Cassete'
    DIG = 'Digital'


#Producto
#1 libros, 2 musica, 3 peliculas

class Producto():
    def __init__(self, codigo, titulo, autor, precio, stock):
        self.codigo = codigo
        self.titulo = titulo
        self.autor = autor
        self.precio = precio
        self.stock = stock

class Libro(Producto):
    def __init__(self,
                  codigo,
                  titulo,
                  autor,
                  precio,
                  stock,
                  editorial,
                  generoLit):
        super().__init__(
                codigo,
                titulo,
                autor,
                precio,
                stock)
        self.editorial = editorial
        self.generoLit = generoLit

    def mostrarProducto(self):
        print('codigo: %s' %self.codigo)
        print('titulo: %s' %self.titulo)
        print('autor: %s' %self.autor)
        print('codigo: %s' %self.codigo)
        print('precio: %i' %self.precio)
        print('stock: %i' %self.stock)
        print('editorial: %s' %self.editorial)
        print('generoLit: %s' %self.generoLit)

class Pelicula(Producto):
    def __init__(self,
                  codigo,
                  titulo,
                  autor,
                  precio,
                  stock,
                  clasificacion,
                  generoPeli):
        super().__init__(
                codigo,
                titulo,
                autor,
                precio,
                stock)
        self.clasificacion = clasificacion
        self.generoPeli = generoPeli
    
    def mostrarProducto(self):
        print('codigo: %s' %self.codigo)
        print('titulo: %s' %self.titulo)
        print('autor: %s' %self.autor)
        print('codigo: %s' %self.codigo)
        print('precio: %i' %self.precio)
        print('stock: %i' %self.stock)
        print('clasificacion: %s' %self.clasificacion)
        print('generoPeli: %s' %self.generoPeli)

class Musica(Producto):
    def __init__(self,
                  codigo,
                  titulo,
                  autor,
                  precio,
                  stock,
                  formato,
                  generoMusi):
        super().__init__(
                codigo,
                titulo,
                autor,
                precio,
                stock)
        self.formato = formato
        self.generoMusi = generoMusi
    
    def mostrarProducto(self):
        print('codigo: %s' %self.codigo)
        print('titulo: %s' %self.titulo)
        print('autor: %s' %self.autor)
        print('codigo: %s' %self.codigo)
        print('precio: %i' %self.precio)
        print('stock: %i' %self.stock)
        print('formato: %s' %self.formato)
        print('generoMusi: %s' %self.generoMusi)

miLibro = Libro('1', '1984', 'Orwell', 1500, 2, 'Anagrama', GeneroLibro.NOVE.value)

miLibro.mostrarProducto()

miPelicula = Pelicula('2', 'Cars', 'Pixar', 2500, 45, ClasificacionCine.ATP.value, GeneroCine.INFA.value)

miPelicula.mostrarProducto()

miDisco = Musica('3', 'Waka Waka', 'Shakira', 5000, 12, FormatoMusica.DIG.value, GeneroMusica.TROP.value)

miDisco.mostrarProducto()