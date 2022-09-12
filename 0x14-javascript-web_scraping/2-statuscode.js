#!/usr/bin/node
/*
Write a script that display the status code of a GET request.
The first argument is the URL to request (GET)
The status code must be printed like this: code: <status code>
*/

const axios = require('axios').default;
axios.get(process.argv[2])
  .then(function (response) {
    console.log('code:', response.status);
  })
  .catch(function (error) {
    console.log('code:', error.response.status);
  });
