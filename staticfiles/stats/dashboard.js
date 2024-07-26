
const dashboard = document.getElementById("dashboard").textContent;
const socket = new WebSocket(`ws://+ ${window.location.host}/ws/Donaters_Dashboard/${dashboard}/`);

console.log("socket",socket);



socket.onmessage = function(e) {
    console.log("server"+e.data);
};


socket.onopen = function(e) {
    socket.send(JSON.stringify({
        "message": "Hello",
        "sender": "varunk"
    }));
};

