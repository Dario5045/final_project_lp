import asyncio

async def enviar_confirmacion(nombre, mesa_id):
    await asyncio.sleep(2)
    print(f"Email enviado a {nombre}: Mesa {mesa_id} reservada.")

async def enviar_cancelacion(nombre, mesa_id):
    await asyncio.sleep(2)
    print(f"Reserva de {nombre} (Mesa {mesa_id}) cancelada.")