class EmptyNameException(Exception):
    def __str__(self):
        return 'El nombre no puede ir vacio'

def hello(name):
    if len(name) == 0:
        raise EmptyNameException
    print('Hola %s' %name)

def conversation(name1='', name2=''):
    try:
        hello(name1)
    except EmptyNameException:
        hello('Unknown person')
    try:
        hello(name2)
    except EmptyNameException:
        hello('Unknown person')
    
conversation('David')