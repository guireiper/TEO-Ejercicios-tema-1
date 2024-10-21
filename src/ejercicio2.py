def calcula_imc(peso, estatura):
    IMC = peso/(estatura**2)
    return IMC

def calcula_estado_nutricional (peso, estatura):
    IMC = calcula_imc(peso,estatura)

    if (IMC < 18.5):
        nutricion = 'Bajo'

    elif(18.5 <= IMC <25):

        nutricion = 'Normal'

    elif(25 <= IMC <30):

        nutricion = 'Sobrepeso'

    elif(IMC >= 30):

        nutricion = 'Obesidad'

    
    return nutricion

peso = float(input('Escribe el peso: '))
estatura = float(input('Escribe la estatura: '))

nutricion = calcula_estado_nutricional(peso, estatura)
print('El valor nutricional de una persona con un peso de',peso,'(KG) y altura',estatura,'(m) es:',nutricion)