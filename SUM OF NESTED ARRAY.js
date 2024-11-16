function sumNestedArray(arr) {
    return arr.flat(Infinity).reduce((sum, num) => sum + num, 0);
}

let nestedArray = [1, [2, [3, [4, 5]]]];
console.log(sumNestedArray(nestedArray)); // Output: 15
