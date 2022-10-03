// Write a function which calculates the average of the numbers in a given list.

// Note: Empty arrays should return 0.


function find_average(array) {
    let sumOfNums = 0
    let average = 0
    if (array.length == 0){
      return 0
    } else {
      for (let i = 0; i <= array.length - 1; i++) {
        sumOfNums += array[i]
      }
      average = sumOfNums / array.length
    }
    return average 
}
