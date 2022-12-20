#!/usr/bin/node
function factorial (a) {
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return a * factorial(a - 1);
  }
}

const args = process.argv;
const num = Number(args[2]);

const result = factorial(num);
console.log(result);
