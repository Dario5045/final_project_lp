# Paradigmas de Programación Utilizados en el Sistema de Reservas de Restaurante

Este proyecto aplica una combinación de paradigmas de programación que permiten una estructura clara, mantenible y funcionalmente rica. A continuación, se detallan los principales paradigmas empleados:

## 1. Paradigma Imperativo

El enfoque imperativo está presente en el flujo principal del programa, donde se especifican paso a paso las instrucciones para gestionar las reservas:

```python
def menu_principal():
    while True:
        print("\n1. Ver mesas disponibles\n2. Hacer reserva\n3. Cancelar reserva\n4. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_mesas_disponibles()
        elif opcion == "2":
            hacer_reserva()
        elif opcion == "3":
            cancelar_reserva()
        elif opcion == "4":
            break
```

## 2. Paradigma Funcional

Se utiliza el paradigma funcional en operaciones puras sin efectos secundarios, como el filtrado de mesas disponibles:

```python
def filtrar_mesas_disponibles(mesas):
    return {id: mesa for id, mesa in mesas.items() if mesa["disponible"]}
```

También se aplican principios de inmutabilidad y funciones de orden superior:

```python
# Cálculo de capacidad total usando reduce (concepto funcional)
from functools import reduce
capacidad_total = reduce(lambda acc, mesa: acc + mesa["capacidad"], mesas.values(), 0)
```

## 3. Paradigma Asincrónico

El manejo de operaciones asíncronas se implementa para simular el envío de notificaciones:

```python
async def enviar_confirmacion(nombre, mesa_id):
    await asyncio.sleep(2)  # Simula demora de red
    print(f"✉️ Email enviado a {nombre}: Mesa {mesa_id} reservada.")
```

Y se integra con el flujo principal mediante async/await:

```python
async def hacer_reserva():
    # ... validaciones
    await enviar_confirmacion(nombre, mesa_id)
```

## 4. Modularidad y Abstracción

El proyecto está organizado en módulos especializados:

```
/reservas-restaurante
├── main.py                # Lógica de flujo principal
├── funciones.py           # Funciones puras y utilitarias
├── api.py                 # Operaciones asincrónicas
└── database.py            # Gestión de datos persistente
```

Esta estructura promueve:

- **Separación de preocupaciones**: Cada módulo maneja una responsabilidad única
- **Reutilización de código**: Funciones como `filtrar_mesas_disponibles` pueden usarse en múltiples contextos
- **Facilidad de mantenimiento**: Los cambios en un módulo tienen mínimo impacto en otros
