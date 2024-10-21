def calcula_imc(peso, estatura):
    IMC = peso/(estatura**2)
    return IMC

peso = float(input('Escribe el peso: '))
estatura = float(input('Escribe la estatura: '))

IMC = calcula_imc(peso, estatura)
print('El IMC de una persona con un peso de',peso,'(KG) y altura',estatura,'(m) es:',IMC)