document.addEventListener('DOMContentLoaded', function() {
    const userData = localStorage.getItem('registeredUser');
    
    if (userData) {
        const user = JSON.parse(userData);
        document.getElementById('welcomeMessage').innerHTML = `
            <h1>Hello, ${user.name}!</h1>
            <p>Your registration ended sucsesfully.</p>
            <p>Your gmail: ${user.email}</p>
        `;
    } else {
        document.getElementById('welcomeMessage').innerHTML = `
            <h1>Your registration didn't ended sucsesfully.</h1>
            <p>please go back on <a href="form.html">and registrate</a>.</p>
        `;
    }
});