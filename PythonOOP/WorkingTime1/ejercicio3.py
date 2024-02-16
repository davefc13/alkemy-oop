def verificar_calificacion(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3)/3
    if promedio >= 6:
        print('Aprobado')
    else:
        print('Reprobado')

verificar_calificacion(8,6,7)