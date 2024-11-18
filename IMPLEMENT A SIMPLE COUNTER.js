function createCounter() {
    let count = 0;
    return function() {
        return ++count;
    };
}

let counter = createCounter();
console.log(counter()); // Output: 1
console.log(counter()); // Output: 2
console.log(counter()); // Output: 3
