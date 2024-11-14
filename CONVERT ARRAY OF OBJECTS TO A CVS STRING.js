function arrayToCSV(arr) {
    const headers = Object.keys(arr[0]).join(',');
    const rows = arr.map(obj => Object.values(obj).join(',')).join('\n');
    return `${headers}\n${rows}`;
}

let data = [
    { name: "Alice", age: 25 },
    { name: "Bob", age: 30 }
];
console.log(arrayToCSV(data));
/* Output:
name,age
Alice,25
Bob,30
*/
