#!/usr/bin/node
const args = process.argv;
const size = Number(args[2]);
let count = 0;

if (size) {
  if (size > 0) {
    while (count < size) {
      let breadth = 0;
      let str = '';
      while (breadth < size) {
        str += 'X' + '';
        breadth++;
      }
      console.log(str.trim());
      count++;
    }
  }
} else {
  console.log('Missing size');
}
