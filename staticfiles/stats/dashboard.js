const socket = new WebSocket(`ws://${window.location.host}/ws/leaderboard/`);

socket.onmessage = function(e) {
    try {
        const data = JSON.parse(e.data);
        if (data.type === 'update') {
            const leaderboardData = JSON.parse(data.data);
            console.log('Received leaderboard data:', leaderboardData);
            updateLeaderboardTable(leaderboardData);
        } else {
            console.error('Unexpected data type:', data.type);
        }
    } catch (error) {
        console.error('Error processing WebSocket message:', error);
    }
};


socket.onopen = function(e) {
    console.log("WebSocket connection established.");
};

socket.onclose = function(e) {
    console.log("WebSocket connection closed.");
};

function updateLeaderboardTable(data) {
    const tbody = document.querySelector('tbody');
    tbody.innerHTML = '';

    data.forEach((item, index) => {
        const donator = item.fields;
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${index + 1}</td>
            <td><a href="/donator/${donator.slug}/">${donator.Donaters_UserID}</a></td>
            <td>businessman</td>
            <td><strong>${donator.value}</strong></td>
        `;
        tbody.appendChild(row);
    });
}
