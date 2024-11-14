function secondLargest(arr) {
    let max = Math.max(...arr);
    arr = arr.filter(num => num !== max);
    return Math.max(...arr);
}

let numbers = [1, 2, 3, 4, 5];
console.log(secondLargest(numbers)); // Output: 4