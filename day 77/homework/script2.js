document.getElementById("myForm").addEventListener("submit", function (event) {
    event.preventDefault(); 

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const age = document.getElementById("age").value;

    console.log("name:", name);
    console.log("gmail:", email);
    console.log("age:", age);
});