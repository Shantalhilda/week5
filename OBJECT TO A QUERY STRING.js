function objectToQueryString(obj) {
    return Object.keys(obj).map(key => encodeURIComponent(key) + '=' + encodeURIComponent(obj[key])).join('&');
}

let params = { name: "Alice", age: 25, city: "New York" };
console.log(objectToQueryString(params)); // Output: "name=Alice&age=25&city=New%20York"
