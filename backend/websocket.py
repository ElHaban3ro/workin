# Importamos la biblioteca necesaria para manejar websockets
import asyncio
import websockets



async def websocket_server(websocket, path):
    # Esperamos a recibir un mensaje del cliente
    message = await websocket.recv()
    print(f"Mensaje recibido: {message}")

    # Respondemos al cliente
    response = "Mensaje recibido"
    await websocket.send(response)

# Iniciamos el servidor
start_server = websockets.serve(websocket_server, "0.0.0.0", 9000)




# Ejecutamos el servidor de forma asíncrona
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()