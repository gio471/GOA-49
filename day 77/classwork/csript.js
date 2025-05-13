// Capturing-ის დროს event'ი იწყება ზემოდან, ანუ ყველაზე გარე ელემენტიდან და გადადის ქვემოთ, სანამ არ მიაღწევს იმ ელემენტს, რომელზეც event'ი მოხდა.
// Bubbling-ის დროს event'ი იწყება იმ ელემენტიდან, რომელზეც event'ი მოხდა, და გადადის ზემოთ


document.getElementById('parent').addEventListener('click', function() {
    console.log('parent clicked');
}, true); // Capturing


document.getElementById('child').addEventListener('click', function() {
    console.log('Child clicked');
}); // Bubbling (default)