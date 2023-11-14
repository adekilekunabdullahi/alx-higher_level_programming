#!/usr/bin/node
function factorial (a) {
  if (isNaN(parseInt(a))) {
    return 1;
  }
  if (a === 0 || a === 1) {
    return 1;
  } else {
    return parseInt(a) * factorial(a - 1);
  }
}
console.log(factorial(process.argv[2]));
