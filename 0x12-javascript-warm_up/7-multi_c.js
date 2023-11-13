#!/usr/bin/node
num = process.argv[2];
if (isNaN(parseInt(num))) {
console.log('Missing number of occurrences');}
else if (num === undefined)
{ console.log('Missing number of occurrences');}
else {
for (let a = 0; a < parseInt(num); a++) {
	console.log('C is fun');
}
}
