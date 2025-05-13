// Capturing-ის დროს event'ი იწყება ზემოდან, ანუ ყველაზე გარე ელემენტიდან და გადადის ქვემოთ, სანამ არ მიაღწევს იმ ელემენტს, რომელზეც event'ი მოხდა.
// Bubbling-ის დროს event'ი იწყება იმ ელემენტიდან, რომელზეც event'ი მოხდა, და გადადის ზემოთ


const next = document.getElementById("next");
const previous = document.getElementById("pre");
const img = document.getElementById("image");

let i = 0;

const images = [
    "./images/image1.jpg",
    "./images/image2.jpg",
    "./images/image3.jpg",
];

next.addEventListener("click", function () {
    i++;
    if (i > 2) {
        i = 0;
    }
    img.src = images[i];
});

previous.addEventListener("click", function () {
    i--;
    if (i < 0) {
        i = 2;
    }
    img.src = images[i];
});