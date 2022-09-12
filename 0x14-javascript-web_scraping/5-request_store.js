#!/usr/bin/node
/*
Write a script that gets the contents of a webpage and stores it in a file.
The first argument is the URL to request
The second argument the file path to store the body response
The file must be UTF-8 encoded
*/

const process = require('process');
const argv = process.argv;
const axios = require('axios').default;
const fs = require('fs');

axios.get(argv[2])
  .then(function (response) {
    fs.writeFile(argv[3], response.data, 'utf8', function (err, data) {
      if (err) {
        console.log(err);
      }
    });
  })
  .catch(function (error) {
    console.log('code: ' + error.response.status);
  });
