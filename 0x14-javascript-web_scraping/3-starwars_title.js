#!/usr/bin/node
/*
Write a script that prints the title of a Star Wars movie where the episode
number matches a given integer
The first argument is the movie ID
https://swapi-api.hbtn.io/api/films/:id
*/

const process = require('process');
const args = process.argv;
const axios = require('axios').default;
const id = args[2];

axios.get(`https://swapi-api.hbtn.io/api/films/${id}`)
  .then(function (response) {
    console.log(response.data.title);
  })
  .catch(function (error) {
    console.log(`code: ${error.response.status}`);
  });
