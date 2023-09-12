function add (a, b) {
  a = parseInt(process.argv[2]);
  b = parseInt(process.argv[3]);

  if (process.argv[2] === undefined || process.argv[3] === undefined) {
    console.log('NaN');
  } else {
    console.log(a + b);
  }
}

add();
