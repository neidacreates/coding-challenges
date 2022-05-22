// Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

// Return your answer as a number.

function sumMix(x){
    let sumOfNum = 0
    for(let i=0;i<x.length;i++){
      let currentNumber = x[i]
  //     console.log(currentNumber)
      currentNumber = Number(currentNumber)
  //     console.log(currentNumber)
      sumOfNum += currentNumber
  //     console.log(sumOfNum)
    }
    return sumOfNum
  }