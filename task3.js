function calculateWaterUsage(Waterusage){
    let total = 0;
for (let i = 0; i < Waterusage.length; i++) {
total += Waterusage[i];
}
return total / Waterusage.length;
}

let Waterusage = [10.5, 78, 90, 17, 99];
let averageWaterusage = calculateWaterUsage(Waterusage);
console.log(`The average score is ${averageWaterusage}`);

