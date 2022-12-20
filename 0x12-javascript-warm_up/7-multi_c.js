#!/usr/bin/node
const args = process.argv;
const count = Number(args[2]);
let i = 0;

if (count) {
  if (count > 0) {
    while (i < count) {
      console.log('C is fun');
      i++;
    }
  }
} else {
  console.log('Missing number of occurences');
}
