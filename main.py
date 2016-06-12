import csv

with open('acusados.csv', encoding='latin3') as fh:
    dr = csv.DictReader(fh)
    casos = [x for x in dr]


for caso in casos:
    count = 1
    try:
        while True:
                sig = casos[casos.index(caso) + count]
                if caso['id'] == sig['id']:
                    count += 1
                    if caso['sexo'] == sig['sexo'] and caso['edad'] == sig['edad'] and caso['tipo'] == sig['tipo']\
                            and caso['modelo'] == sig['modelo'] and caso['rol'] == sig['rol']:
                        sig['repetido'] = 1
                else:
                    break
    except IndexError:
        break

with open('acusados_result.csv', 'w', newline='') as fh:
    fieldnames = ['id', 'rol', 'sexo', 'edad', 'tipo', 'modelo', 'repetido']
    dw = csv.DictWriter(fh, delimiter=',', fieldnames=fieldnames)
    dw.writeheader()
    for x in casos:
        dw.writerow(x)

# for x in casos:
#     print(x)

