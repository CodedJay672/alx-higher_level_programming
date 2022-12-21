#!/usr/bin/node
const dict = require('./101-data.js').dict;

const dictEntries = Object.entries(dict);
const dictVals = Object.values(dict);
const uniqVals = [...new Set(dictVals)];
const newDict = {};

for (const j in uniqVals) {
  const list = [];
  for (const k in dictEntries) {
    if (dictEntries[k][1] === uniqVals[j]) list.unshift(dictEntries[k][0]);
  }
  newDict[uniqVals[j]] = list;
}
console.log(newDict);
