#!/usr/bin/node
num = process.argv[2];
if (!isNaN(parseInt(num))) {
for (let a = 0; a < parseInt(num); a++) {
	row = '';
	for (let b = 0; b < parseInt(num); b++){
		row += 'X';
}
	console.log(row);
}
}
else {
console.log('Missing size');
}
