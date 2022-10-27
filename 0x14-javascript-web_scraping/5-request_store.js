#!/usr/bin/node
const fs = require('fs');
const request = require('request');
const url = process.argv[2];
const file = process.argv[3];

request(url, function (err, response) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(file, response.body, 'utf-8', function (err) {
      if (err) { console.log(err); }
    });
  }
});