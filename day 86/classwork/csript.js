document.getElementById('userForm').addEventListener('submit', function(e) {
    e.preventDefault();
    

    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const age = document.getElementById('age').value;
    

    const person = {
        name: name,
        email: email,
        age: age
    };
    

    let personCount = localStorage.length;
    const personKey = 'person' + (personCount + 1);
    

    while (localStorage.getItem(personKey)) {
        personCount++;
    }

    localStorage.setItem('person' + (personCount + 1), JSON.stringify(person));

    document.getElementById('userForm').reset();
    
    alert('User information saved successfully!');
});