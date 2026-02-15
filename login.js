document.getElementById('loginForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    const data = Object.fromEntries(new FormData(e.target));

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });

        if (response.ok) {
            // Redirect to the outreach engine on success
            window.location.href = 'chat.html';
        } else {
            alert('Invalid credentials in Cluster1.');
        }
    } catch (error) {
        console.error('Connection error:', error);
    }
});