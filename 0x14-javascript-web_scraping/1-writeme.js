#!/usr/bin/node
const data = process.argv[3];
const file = process.argv[2];
const fs = require('fs');
fs.writeFile(file, data, function (error) {
  if (error) console.log(error);
});
