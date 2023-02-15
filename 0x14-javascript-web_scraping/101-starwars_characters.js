#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, function (err, response, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printName(characters, 0);
  }
});

function printName (characters, idx) {
  request.get(characters[idx], function (error, response, body1) {
    if (!error) {
      console.log(JSON.parse(body1).name);
      if (idx + 1 < characters.length) {
        printName(characters, idx + 1);
      }
    }
  });
}
