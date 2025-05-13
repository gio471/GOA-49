const next = document.getElementById("next");
const previous = document.getElementById("pre");
const img = document.getElementById("image");

let i = 0;

const images = [
    "./images/image1.jpg",
    "./images/image2.jpg",
    "./images/image3.jpg",
    "./images/image4.jpg",
    "./images/image5.jpg",
];

next.addEventListener("click", function () {
    i++;
    if (i > 5) {
        i = 0;
    }
    img.src = images[i];
});

previous.addEventListener("click", function () {
    i--;
    if (i < 0) {
        i = 5;
    }
    img.src = images[i];
});