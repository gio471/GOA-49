const regForm = document.getElementById("register");
const loginForm = document.getElementById("login");
const usersDiv = document.getElementById("users-data");

const admin = {
    username: "Nika",
    email: "nikoloz0812@gmail.com",
    password: "12345",
    isAdmin: true
}

let users = JSON.parse(localStorage.getItem("users")) || [admin];
localStorage.setItem("users", JSON.stringify(users));

const setLocalStorage = (key, value) => {
    localStorage.setItem(key, JSON.stringify(value));
}

function Account(username, email, password) {
    return { username, email, password, isAdmin: false };
}

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
    setLocalStorage("users", users);
    alert("Registered successfully");
    regForm.reset();
}

const deleteUser = (isAdmin, delEmail) => {
    users = users.filter(user => user.email !== delEmail);
    setLocalStorage("users", users);
    
    if(isAdmin) {
        renderAllUsers(users[0]);
    } else {
        usersDiv.innerHTML = "";
    }
}

const toggleAdmin = (email) => {
    users = users.map(user => {
        if (user.email === email) {
            user.isAdmin = !user.isAdmin;
        }
        return user;
    });
    setLocalStorage("users", users);
    renderAllUsers(users[0]);
}

const renderAllUsers = (adminAcc) => {
    usersDiv.innerHTML = `
        <div>
            <h3>Admin: ${adminAcc.username}</h3>
            <p>Email: ${adminAcc.email}</p>
            <button onclick="handleLogout()">Logout</button>
        </div>
    `;
    
    users.slice(1).forEach(user => {
        usersDiv.innerHTML += `
            <div>
                <h3>Username: ${user.username}</h3>
                <p>Email: ${user.email}</p>
                <p>Password: ${user.password}</p>
                <p>Role: ${user.isAdmin ? 'Admin' : 'User'}</p>
                <button onclick="deleteUser(true, '${user.email}')">Delete</button>
                <button onclick="toggleAdmin('${user.email}')">Toggle Role</button>
            </div>
        `;
    });
}

const renderUser = (user) => {
    usersDiv.innerHTML = `
        <div>
            <h3>Username: ${user.username}</h3>
            <p>Email: ${user.email}</p>
            <p>Password: ${user.password}</p>
            <button onclick="deleteUser(false, '${user.email}')">Delete</button>
            <button onclick="handleLogout()">Logout</button>
        </div>
    `;
}

const handleLogIn = () => {
    const email = loginForm.email.value;
    const password = loginForm.password.value;

    for(const user of users) {
        if(user.email === email && user.password === password) {
            usersDiv.innerHTML = "";
            if(user.isAdmin) {
                renderAllUsers(user);
            } else {
                renderUser(user);
            }
            loginForm.reset();
            return;
        }
    }

    alert("User not found");
}

const handleLogout = () => {
    usersDiv.innerHTML = "";
}

regForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleRegister();
})

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    handleLogIn();
})