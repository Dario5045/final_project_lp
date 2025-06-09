from funciones import filtrar_mesas_disponibles
from api import enviar_confirmacion
from api import enviar_cancelacion
from database import mesas
from database import reservas
import asyncio

async def cancelar_reserva():
    nombre = input("Nombre asociado a la reserva: ").strip()
    mesa_id = input("ID de la mesa a cancelar: ").strip()

    reserva_encontrada = None
    for reserva in reservas:
        if reserva["nombre"] == nombre and reserva["mesa"] == mesa_id:
            reserva_encontrada = reserva
            break
    if reserva_encontrada:
        mesas[mesa_id]["disponible"] = True
        reservas.remove(reserva_encontrada)
        await enviar_cancelacion(nombre, mesa_id)

    else:
        print(f"No se encontro la reserva. Verifique nombre y ID.")



async def hacer_reserva():
    while True:
        nombre = input("Nombre: ")

        while not nombre:
            nombre = input("Nombre no puede estar vacio: ").strip()

        mesa_id = input("ID de mesa: ")

        if not mesa_id.isdigit() or mesa_id not in mesas:
            print("ERROR: Ingrese numero de mesa valido.")
            mesas_libres = filtrar_mesas_disponibles(mesas)
            print("Mesas disponibles:", ",".join(mesas_libres.keys()))
            continue

        if not mesas[mesa_id]["disponible"]:
            print("\n Esa mesa esta ocupada\n. Mesas libres:")
            mesas_libres = filtrar_mesas_disponibles(mesas)
            for id, mesa in mesas_libres.items():
                print(f"Mesa {id} (Capacidad: {mesa['capacidad']})")
            opcion = input("\n Intentar con otra mesa? (S/N): ").upper()
            if opcion != "S":
                break
            continue

        reservas.append({"nombre": nombre, "mesa": mesa_id})
        mesas[mesa_id]["disponible"] = False
        await enviar_confirmacion(nombre, mesa_id)
        print("Reserva exitosa!!!")
        break
async def menu_principal():
    while True:
        print("\n----MENU PRINCIPAL----")
        print("\n1. Ver mesas disponibles\n2. Hacer reserva\n3. Cancelar reserva\n4. Salir")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            mesas_libres = filtrar_mesas_disponibles(mesas)
            for id, mesa in mesas_libres.items():
                print(f"Mesa {id} (Capacidad: {mesa['capacidad']})")
        elif opcion == "2":
            await hacer_reserva()
        elif opcion == "3":
            await cancelar_reserva()
        elif opcion == "4":
            break
        else:
            print("Opcion no valida.")

async def main():
    await menu_principal()

if __name__ == "__main__":
    asyncio.run(main())