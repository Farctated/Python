function findEfficientBulbs(serialNumbers) {
    const efficientSerialNumbers = [];
    // Write your code here
    for(let i = 0; i < serialNumbers.length; i++){
        if (serialNumbers[i].toString().length === 6 && serialNumbers[i] % 2 !== 0){
            efficientSerialNumbers.push(serialNumbers[i])

        }
    }
    console.log(efficientSerialNumbers)
    return efficientSerialNumbers;
}
const serialNumbers = [32438, 34193, 149143, 4329429, 98537, 238791, 23492, 298342]
findEfficientBulbs(serialNumbers)