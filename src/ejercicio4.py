def lee_numeros():
    res=[]
    tam = int(input('Cuanto numeros quieres almacenar: '))
    i=0

    while i < tam:
        i = i+1
        num = int(input(f'Escriba el numero {i} para saberlo: '))
        res.append(num)
        

    return res

lista = lee_numeros()

print('El mayor número de la lista: ', max(lista))

media = sum(lista)/len(lista)

print('La media de la lista es:',media)

pares = [num for num in lista if num % 2 == 0]

print('Los pares de la lista:',pares)

mayores = [num for num in lista if num > 10]

print('Mayores a 10:',mayores)