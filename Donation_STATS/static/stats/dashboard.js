const socket = new WebSocket(`ws://${window.location.host}/ws/leaderboard/`);

socket.onmessage = function(e) {
    const data = JSON.parse(e.data);
    if (data.type === 'update') {
        const leaderboardData = JSON.parse(data.data);
        updateLeaderboardTable(leaderboardData);
    }
};

socket.onopen = function(e) {
    console.log("WebSocket connection established.");
};

socket.onclose = function(e) {
    console.log("WebSocket connection closed.");
};

function updateLeaderboardTable(data) {
    // Update the leaderboard table with the new data
    const tbody = document.querySelector('tbody');
    tbody.innerHTML = '';

    data.forEach(item => {
        const donator = JSON.parse(item.fields);
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${donator.username}</td>
            <td>${donator.value}</td>
        `;
        tbody.appendChild(row);
    });
}
