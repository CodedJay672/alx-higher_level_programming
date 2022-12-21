#!/usr/bin/node
const filepath = require('fs');

const args1 = filepath.readFileSync(process.argv[2].toString());
const args2 = filepath.readFileSync(process.argv[3].toString());
filepath.writeFileSync(process.argv[4], args1 + args2);
