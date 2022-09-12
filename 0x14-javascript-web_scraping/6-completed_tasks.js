#!/usr/bin/node
/*
The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
https://developer.mozilla.org/es/docs/Web/JavaScript/Reference/Global_Objects
/isNaN
*/

const axios = require('axios').default;
axios({
  method: 'get',
  url: process.argv[2]
})
  .then(function (response) {
    const dict = {};
    for (const Data in response.data) {
      const user = response.data[Data].userId;
      const ended = response.data[Data].completed;
      if (isNaN(dict[user]) && ended) {
        dict[user] = 1;
      } else if (ended) {
        dict[user] += 1;
      }
    }
    console.log(dict);
  });
