def filtrar_mesas_disponibles(mesas):
    return {id: mesa for id, mesa in mesas.items() if mesa["disponible"]}

def calcular_capacidad_total(mesas):
    return sum(mesa["capacidad"] for mesa in mesas.values())