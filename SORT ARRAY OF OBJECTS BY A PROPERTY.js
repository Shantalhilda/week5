function sortByProperty(arr, property) {
    return arr.sort((a, b) => (a[property] > b[property] ? 1 : -1));
}

let people = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 22 },
    { name: "Charlie", age: 30 }
];
console.log(sortByProperty(people, "age")); // Output: Sorted array by age
