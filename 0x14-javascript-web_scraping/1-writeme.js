#!/usr/bin/node
/*
Write a script that writes a string to a file.
Arg[2]= path of the file
Arg[3]= content of the file
*/
const argv = process.argv;
const fs = require('fs');
fs.writeFile(argv[2], argv[3], 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  }
});
