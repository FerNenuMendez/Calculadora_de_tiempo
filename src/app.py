
def calcularaños(m):
    an = round(m/525600)
    return an


def calcularmeses(m):
    cantidad = round(m % 525600)
    ms = round(cantidad/43200)
    return ms


def calculardias(m):
    cantidad = round(m % 43.200)
    ms = round(cantidad / 1440)
    return ms


def calcularhoras(m):
    hs = round(m % 1440)
    horas = round(hs/60)
    return horas


def calcularminutos(m):
    ms = round(m % 60)
    return ms


def horasyminutos(m):
    print(f"{time} minutos son  {calcularaños(m)} año/s, {calcularmeses(m)} meses, {calculardias(m)} dias, {calcularhoras(m)} horas y {calcularminutos(m)} minutos")


time = int(input("Ingrese el numero de minutos que desea transformar: "))
print(horasyminutos(time))
