const io = require('socket.io-client');
const socket = io.connect('http://localhost:5000');

socket.on('dash_event', function(data) {
    console.log('Received event from Dash:', data);
    // Handle actions from Dash application here
    socket.emit('js_event', { message: 'Event received by JS' });
});