#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (err, response) {
  if (err) console.log(err);
  else if (response.statusCode === 200) {
    const body = JSON.parse(response.body);
    console.log(body.title);
  } else {
    console.log('Erorr Code:' + response.statusCode);
  }
});
