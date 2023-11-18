#!/usr/bin/node
const num = process.argv[2];
if (!isNaN(parseInt(num))) {
  for (let a = 0; a < parseInt(num); a++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
