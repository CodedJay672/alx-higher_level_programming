#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
request(url, function (err, response, body) {
  if (!err) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todos) => {
      if (todos.completed && completed[todos.userId] === undefined) {
        completed[todos.userId] = 1;
      } else if (todos.completed) {
        completed[todos.userId] += 1;
      }
    });
    console.log(completed);
  }
});
