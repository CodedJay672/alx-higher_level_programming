#!/usr/bin/node

exports.esrever = function (list) {
  let length = list.length - 1;
  let index = 0;
  const revList = [];

  while (length >= 0) {
    revList[index] = list[length];
    length--;
    index++;
  }
  return revList;
};
