//Example 1: A Simple Greeting Function
//Define a function that greets someone in Uganda:
function greetUgandan(name) {
console.log(`Hello ${name}, welcome to Uganda!`);
}
greetUgandan("John");



//Example 2: Calculate Taxi Fare
function calculateTaxiFare(distance, farePerKm) {
   return distance * farePerKm;
}

let distanceToWandegeya = 10; // Distance in kilometers
let farePerKm = 5000; // UGX
let totalFare = calculateTaxiFare(distanceToWandegeya, farePerKm);
console.log(`Total taxi fare to Wandegeya is UGX ${totalFare}`);





//Example 3: Calculating the Average Score of Students
//Imagine you are marking exams in a Ugandan school and need to calculate the average score.
function calculateAverage(scores) {
let total = 0;
for (let i = 0; i < scores.length; i++) {
total += scores[i];
}
return total / scores.length;
}
let studentScores = [85, 78, 92, 67, 88];
let averageScore = calculateAverage(studentScores);
console.log(`The average score is ${averageScore}`);


//Anonymous Function Example:
let greet = function(name) {
  console.log(`Hello ${name}, how is Uganda treating you?`);
};
greet("Paul");

//Arrow Function Example:
let greet = (name) => {
     console.log(`Hello ${name}, welcome to the JavaScript world!`);
};
greet("Paul"); 




//Example 5: Calculate Revenue for a Farmer
function calculateRevenue(pricePerBunch, numberOfBunches) {
return pricePerBunch * numberOfBunches;
}
let pricePerBunch = 15000; // UGX
let bunchesSold = 30; // Number of bunches sold
let revenue = calculateRevenue(pricePerBunch, bunchesSold);
console.log(`Total revenue for selling matooke is UGX ${revenue}`);




//Example 6: Calculate School Fees with Default Boarding Fee
function calculateFees(tuitionFee, boardingFee = 500000) {
   return tuitionFee + boardingFee;
}
let totalFeesWithBoarding = calculateFees(1500000);
console.log(`Total school fees (with boarding) are UGX
${totalFeesWithBoarding}`);
let totalFeesWithoutBoarding = calculateFees(1500000, 0);
console.log(`Total school fees (without boarding) are UGX
${totalFeesWithoutBoarding}`);




//Example 7: Calculate Factorial (Recursive)
function factorial(n) {
  if (n === 1) {
    return 1;
} else {
   return n * factorial(n - 1);
}
}
let result = factorial(5);
console.log(`The factorial of 5 is ${result}`);



//Example 8: Local and Global Scope
let globalVar = "I'm a global variable";
function testScope() {
   let localVar = "I'm a local variable";
   console.log(globalVar); // Accessible inside the function
   console.log(localVar); // Accessible inside the function
}
testScope();
console.log(globalVar); // Accessible outside the function
// console.log(localVar); // Error: localVar is not defined



//Example 9: Using IIFE
(function () {
console.log("This function runs immediately!");
})();



////Example 10: Higher-Order Function with a Callback
function processPayment(amount, paymentCallback) {
console.log(`Processing payment of UGX ${amount}`);
paymentCallback();
}
function onPaymentSuccess() {
console.log("Payment successful!");
}
processPayment(50000, onPaymentSuccess);