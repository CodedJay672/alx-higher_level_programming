#!/usr/bin/node
const newList = require('./100-data.js').list;
const mapList = newList.map(function (number, index) {
  return number * index;
});

console.log(newList);
console.log(mapList);
