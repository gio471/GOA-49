function exsclusiveForEach(array, call) {
    for (let i = 0; i < array.length; i++) {
    call(array[i],array);
    }
}


function superdupercopyofMap(array, call) {
    const myArr = [];
    for (let i = 0; i < array.length; i++) {
        myArr.push(call(array[i], i, array));
    }
    return myArr;
}
