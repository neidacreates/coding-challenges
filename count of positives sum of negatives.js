// Given an array of integers.

// Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

// If the input is an empty array or is null, return an empty array.
// Example

// For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

function countPositivesSumNegatives(input) {
    let tempArray = []
    let countPos = 0
    let sumNeg = 0
    if (input === null || input.length === 0){
      return []      
      }else {
        for (let i = 0; i <= input.length-1; i++){
          if(input[i] > 0){
            countPos += 1
          }else if (input[i] < 0){
            sumNeg += input[i]
        }
      }
        if(countPos == 0 && sumNeg == 0) {
          return []
        }
        tempArray.push(countPos)
        tempArray.push(sumNeg)
        return tempArray 
      }
  }

// countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])