const regForm = document.getElementById("register");
const loginForm = document.getElementById("login");
const userInfoDiv = document.getElementById("userInfo");
const adminPanelDiv = document.getElementById("adminPanel");
const logoutBtn = document.getElementById("logoutBtn");
const usersListDiv = document.getElementById("usersList");


let users = JSON.parse(localStorage.getItem('users')) || [];


const adminAccount = {
    username: 'admin',
    email: 'admin@example.com',
    password: 'admin123',
    isAdmin: true
};


if (!users.some(user => user.email === adminAccount.email)) {
    users.push(adminAccount);
    localStorage.setItem('users', JSON.stringify(users));
}

function Account(username, email, password, isAdmin = false) {
    return { username, email, password, isAdmin };
}

let currentUser = null;

const handleRegister = () => {
    for(const user of users) {
        if(user.email === regForm.email.value) {
            alert("Email is already registered");
            return;
        }
    }

    const username = regForm.username.value;
    const email = regForm.email.value;
    const password = regForm.password.value;

    users.push(new Account(username, email, password));
    

    localStorage.setItem('users', JSON.stringify(users));
    
    console.log(users);
    alert("Registered successfully");
    regForm.reset();
}

const handleLogIn = () => {
    const email = loginForm.email.value;
    const password = loginForm.password.value;

    for(const user of users) {
        if(user.email === email && user.password === password) {
            currentUser = user;
            
            // Display user info
            document.getElementById("info-username").textContent = user.username;
            document.getElementById("info-email").textContent = user.email;
            document.getElementById("info-password").textContent = user.password;
            userInfoDiv.style.display = 'block';
            
            // If admin, show admin panel
            if (user.isAdmin) {
                adminPanelDiv.style.display = 'block';
                displayAllUsers();
            } else {
                adminPanelDiv.style.display = 'none';
            }
            
            loginForm.reset();
            return;
        }
    }

    alert("User not found");
}

const handleLogOut = () => {
    currentUser = null;
    userInfoDiv.style.display = 'none';
    adminPanelDiv.style.display = 'none';
}

const displayAllUsers = () => {
    usersListDiv.innerHTML = '';
    
    users.forEach((user, index) => {
        const userDiv = document.createElement('div');
        userDiv.className = 'user-item';
        userDiv.innerHTML = `
            <p><strong>Username:</strong> ${user.username}</p>
            <p><strong>Email:</strong> ${user.email}</p>
            <p><strong>Admin:</strong> ${user.isAdmin ? 'Yes' : 'No'}</p>
            ${!user.isAdmin ? `<button onclick="deleteUser(${index})">Delete User</button>` : ''}
        `;
        usersListDiv.appendChild(userDiv);
    });
}

const deleteUser = (index) => {
    if (confirm('Are you sure you want to delete this user?')) {
        users.splice(index, 1);
        localStorage.setItem('users', JSON.stringify(users));
        displayAllUsers();
        alert('User deleted successfully');
    }
}


regForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleRegister();
})

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleLogIn();
})

logoutBtn.addEventListener("click", (e) => {
    e.preventDefault();
    handleLogOut();
});