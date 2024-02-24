// Crear una nueva conexión WebSocket.
var socket = new WebSocket('ws://localhost:8080');

// Conexión abierta
socket.addEventListener('open', function (event) {
    socket.send('Hello Server!');
});

// Escuchar mensajes
socket.addEventListener('message', function (event) {
    console.log('Message from server: ', event.data);
});

// Escuchar errores
socket.addEventListener('error', function (event) {
    console.log('Error: ', event);
});

// Conexión cerrada
socket.addEventListener('close', function (event) {
    console.log('Server connection closed: ', event);
});