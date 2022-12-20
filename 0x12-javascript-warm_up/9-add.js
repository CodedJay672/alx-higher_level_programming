#!/usr/bin/node

const args = process.argv;
const len = args.length;

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

if (len === 4) {
  const a = Number(args[2]);
  const b = Number(args[3]);
  add(a, b);
} else {
  console.log('NaN');
}
