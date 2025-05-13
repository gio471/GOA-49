document.getElementById('registrationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    

    localStorage.setItem('registeredUser', JSON.stringify({ name, email }));
    

    window.location.href = 'welcome.html';
});