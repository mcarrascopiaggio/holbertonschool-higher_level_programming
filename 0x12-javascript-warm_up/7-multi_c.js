#!/usr/bin/node
const { argv } = require('process');
const text = 'C is fun';
if (parseInt(argv[2])) {
  for (let x = 0; x < parseInt(argv[2]); x++) {
    console.log(text);
  }
} else {
  console.log('Missing number of occurrences');
}
