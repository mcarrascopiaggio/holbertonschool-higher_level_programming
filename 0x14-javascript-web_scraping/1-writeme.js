#!/usr/bin/node
/*
Write a script that writes a string to a file.
Arg[2]= path of the file
Arg[3]= content of the file
*/

const fileName = process.argv[2];
const content = process.argv[3];
const fs = require('fs');

fs.writeFile(fileName, content, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
