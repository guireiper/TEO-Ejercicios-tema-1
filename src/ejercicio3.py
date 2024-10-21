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

def imprime_estados_nutricionales(personas):
    k = len(personas)
    i=0
    for k in personas:

        IMC = float(calcula_imc(personas[i][0],personas[i][1]))
        nutricion = calcula_estado_nutricional(personas[i][0],personas[i][1])
        i=i+1
        print('El IMC de la persona',i,'es',IMC,'y su estado nutricional es',nutricion)

personas = [
    (60.0, 1.6),
    (75.4, 1.75),
    (87.9, 1.69),
    (45.1, 1.65)
]

imprime_estados_nutricionales(personas)