#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + movieID;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    if (JSON.parse(body).detail === 'Not found') {
      console.log(JSON.parse(body).detail);
    } else {
      console.log(JSON.parse(body).title);
    }
  }
});
