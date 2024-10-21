from datetime import *

def calcula_dia_semana():
    
    dia = int(input('Que dia nacistes: '))
    mes = int(input('Que mes nacistes: '))
    año = int(input('Que año nacistes: '))
    fecha = date(año, mes, dia)
    semana = fecha.strftime("%A")

    return semana


semana = calcula_dia_semana()

print('Nacisteis en',semana)