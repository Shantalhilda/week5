function objectsEqual(obj1, obj2) {
    let keys1 = Object.keys(obj1);
    let keys2 = Object.keys(obj2);

    if (keys1.length !== keys2.length) {
        return false;
    }

    for (let key of keys1) {
        if (obj1[key] !== obj2[key]) {
            return false;
        }
    }

    return true;
}

let obj1 = { name: "Alice", age: 25 };
let obj2 = { name: "Alice", age: 25 };
let obj3 = { name: "Bob", age: 30 };

console.log(objectsEqual(obj1, obj2)); // Output: true
console.log(objectsEqual(obj1, obj3)); // Output: false
