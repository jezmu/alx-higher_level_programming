#!/usr/bin/node
const fs = require('fs');

const file = process.argv[2];
const txt = process.argv[3];
fs.writeFile(file, txt, 'utf-8', function (err) {
  if (err) { console.log(err); }
});
