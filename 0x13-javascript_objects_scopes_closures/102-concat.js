#!/usr/bin/node
const filepath = require('fs');

const args_1 = filepath.readFileSync(process.argv[2].toString());
const args_2 = filepath.readFileSync(process.argv[3].toString());
filepath.writeFileSync(process.argv[4], args_1 + args_2);
