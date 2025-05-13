let clas = document.getElementsByClassName("class");
console.log(clas);


// ID-ით წამოღება
let elementById = document.querySelector("#Id");
console.log(elementById);

// კლასით წამოღება
let elementByClass = document.querySelector(".class-1");
console.log(elementByClass);


let imgElement = document.querySelector("img");
imgElement.src = "./fish.jpg"; 
imgElement.width = 300; 


let pElement = document.querySelector("p");
pElement.style.color = "red"; 
pElement.style.backgroundColor = "yellow"; 
pElement.style.fontSize = "20px";



let newParagraph = document.createElement("p");
let textNode = document.createTextNode("this is new p!");
newParagraph.appendChild(textNode);
let targetDiv = document.querySelector("#newp");
targetDiv.appendChild(newParagraph);


