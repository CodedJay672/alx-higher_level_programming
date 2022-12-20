#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w = 0, h = 0) {
    if (w <= 0 || h <= 0) return this;
    this.width = w;
    this.height = h;
  }

  print () {
    let count = 0;

    while (count < this.height) {
      let prnt = 0;
      let str = '';
      while (prnt < this.width) {
        str += 'X' + '';
        prnt++;
      }
      console.log(str.trim());
      count++;
    }
  }
};
