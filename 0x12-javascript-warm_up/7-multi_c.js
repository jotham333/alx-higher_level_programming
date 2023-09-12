const arg = process.argv[2];
const intValue = parseInt(arg);

if (process.argv[2] === undefined) {
  console.log('Missing number of occurences');
} else if (isNaN(intValue) || intValue < 1) {
  process.exit(1);
} else {
  for (let i = 0; i < intValue; i++) {
    console.log('C is fun');
  }
}
