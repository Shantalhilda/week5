function getUniqueElements(arr) {
    return [...new Set(arr)];
}

let numbers = [1, 2, 2, 3, 4, 4, 5];
console.log(getUniqueElements(numbers)); // Output: [1, 2, 3, 4, 5]
