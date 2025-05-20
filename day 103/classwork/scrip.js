// Promise არის ობიექტი, რომელიც წარმოადგენს ასინქრონული ოპერაციის საბოლოო დასრულებას.

function getServerData() {
return new Promise((resolve, reject) => {
    setTimeout(() => {
    const success = true; 
    
    if (success) {
        resolve({
        name: "Giorgi",
        age: 1655973957,
        city: "somwhere"
        });
    } else {
        reject("server error");
    }
    }, 1500);
});
}


function myFunc() {
return new Promise((resolve, reject) => {
    setTimeout(() => {
    reject({
        statusCode: 404,
        message: "Data not found",
        details: "URL information or resource no longer exists."
    });
    }, 2000);
});
}


