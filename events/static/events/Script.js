document.addEventListener('DOMContentLoaded', () => {
    const ws = new WebSocket('ws://127.0.0.1:8000/ws/administrator');

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.type === 'update') {
            updateList(data.model, data.items);
        }
    };

    ws.onclose = () => {
        console.log('WebSocket connection closed');
    };

    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', (event) => {
            event.preventDefault();
            const formData = new FormData(form);
            
            // Convert FormData to a JSON string if needed
            const formDataObject = {};
            formData.forEach((value, key) => {
                formDataObject[key] = value;
            });
            formDataObject["action"]="Update"
            const formDataJson = JSON.stringify(formDataObject);

            // Send the JSON string over WebSocket
            ws.send(formDataJson);

            // Optionally, handle any additional UI updates or feedback here
            form.reset();
        });
    });

    function updateList(model, items) {
        const list = document.querySelector(`#${model}_list`);
        list.innerHTML = '';
        items.forEach(item => {
            const li = document.createElement('li');
            li.textContent = `${item.name} - `;
            const editLink = document.createElement('a');
            editLink.href = item.edit_url;
            editLink.textContent = 'Edit';
            li.appendChild(editLink);
            li.append(' - ');
            const deleteLink = document.createElement('a');
            deleteLink.href = item.delete_url;
            deleteLink.textContent = 'Delete';
            li.appendChild(deleteLink);
            list.appendChild(li);
        });
    }
});
