class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      this.width = undefined;
      this.height = undefined;
    } else {
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
