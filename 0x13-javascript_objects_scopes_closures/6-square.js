#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

module.exports = class Square extends Rectangle {
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
