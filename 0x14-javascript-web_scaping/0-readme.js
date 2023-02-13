#!/usr/bin/node
const file = process.argv[2];
const rf = require('fs');
rf.readFile(file, 'utf-8', function (err, data) {
  console.log(err || data);
});
