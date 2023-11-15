#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((Number.isInteger(w) && w > 0) && (Number.isInteger(h) && h > 0)) {
      this.width = w;
      this.height = h;
    }
  }
  print () {
    for (let a = 0; a < this.height; a++) {
      let rec = '';
      for (let b = 0; b < this.width; b++) {
        rec += 'X';
      }
      console.log(rec);
    }
  }
}
module.exports = Rectangle;
