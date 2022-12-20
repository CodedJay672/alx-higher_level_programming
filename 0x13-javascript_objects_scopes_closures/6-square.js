#!/usr/bin/node

const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      let height = 0;
      while (height < this.height) {
        let width = 0;
        let str = '';
        while (width < this.width) {
          str += c + '';
          width++;
        }
        console.log(str.trim());
        height++;
      }
    } else super.print();
  }
};
