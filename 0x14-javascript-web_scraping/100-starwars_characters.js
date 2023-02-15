#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url + id, function (err, response, body) {
  if (err) console.log(err);
  const characters = JSON.parse(body).characters;
  for (const name of characters) {
    request.get(name, function (error, response, body1) {
      if (error) console.log(error);
      console.log(JSON.parse(body1).name);
    });
  }
});
