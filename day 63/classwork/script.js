let x = prompt("enter your score")

if (x>=90 & x<=100){
    console.log("grade:A");
} else if (x>=80 & x<90){
    console.log("grade:B");
} else if (x>=70 & x<80){
    console.log("grade:C");
} else if (x>=60 & x<70){
    console.log("grade:D");
} else {
    console.log("grade:F")
}



let y = prompt("enter your age")

if (y<13) {
    console.log("you are kid")
} else if (y>=13 & y<18){
    console.log("you arenot adult yet")
} else{
    console.log("you are an adult")
}

let i=0
while (i<=100){
    console.log(i);
    i++;
}


for(let a=5; a<=10; i++ ){
    console.log(a)
}