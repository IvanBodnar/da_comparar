import csv

with open('acusados.csv', encoding='latin3') as fh:
    dr = csv.DictReader(fh)
    casos = [x for x in dr]


for caso in casos:
    # Contador para subir el numero de indice dentro del while
    count = 1
    # Hay que envolver el while en un try-except porque al final se pasa de
    # indice y tira una IndexError
    try:
        while True:
            # sig en la primera iteracion va a ser igual al item
            # con indice[indice de caso + count], o sea que va a subir en 1
            # con cada iteracion del while si se cumple la condicion del if
            sig = casos[casos.index(caso) + count]
            # Chequea que sean el mismo caso (misma id)
            if caso['id'] == sig['id']:
                # Se eleva count en 1 porque es el mismo caso
                count += 1
                # Siendo el mismo caso, se chequean las demas condiciones
                if caso['sexo'] == sig['sexo'] and caso['edad'] == sig['edad'] and caso['tipo'] == sig['tipo']\
                        and caso['modelo'] == sig['modelo'] and caso['rol'] == sig['rol']:
                    # Si es un repetido, se agrega un 1 en la columna 'repetido'
                    sig['repetido'] = 1
            # Si ya no es el mismo caso, se vuelve al for para evaluar el siguiente
            else:
                break
    except IndexError:
        break

# Usar siempre newline='' cuando salvamos un csv con DictWriter
with open('acusados_result.csv', 'w', newline='') as fh:
    fieldnames = ['id', 'rol', 'sexo', 'edad', 'tipo', 'modelo', 'repetido']
    dw = csv.DictWriter(fh, delimiter=',', fieldnames=fieldnames)
    dw.writeheader()
    for x in casos:
        dw.writerow(x)

# for x in casos:
#     print(x)

