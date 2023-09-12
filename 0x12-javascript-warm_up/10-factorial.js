function calculateFactorial (n) {
  // Base case: factorial of 0 or NaN is 1
  if (isNaN(n) || n === 0) {
    return 1;
  }

  // Recursive case: multiply n by the factorial of (n-1)
  return n * calculateFactorial(n - 1);
}

const arg = process.argv[2];
const intValue = parseInt(arg);

const result = calculateFactorial(intValue);
console.log(`The factorial of ${intValue} is ${result}`);
