function arrayDifference(arr1, arr2) {
    return arr1.filter(x => !arr2.includes(x));
}

let array1 = [1, 2, 3, 4];
let array2 = [3, 4, 5, 6];
console.log(arrayDifference(array1, array2)); // Output: [1, 2]

