// let num1 = Number(prompt("Enter number: "));
// let num2 = Number(prompt("Enter number: "));

// console.log(num1 + num2)


// let name = String(prompt("Enter your name: "));
// alert(`Hello, ${name}!`);



document.getElementById("nameForm").addEventListener("submit", function(event) {
    event.preventDefault();

    const name = document.getElementById("nameInput").value;

    console.log(`user name: ${name}`);
});