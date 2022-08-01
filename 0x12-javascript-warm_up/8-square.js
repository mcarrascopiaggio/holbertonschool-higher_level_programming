#!/usr/bin/node
const { argv } = require('process');
const side = parseInt(argv[2]);
let i;

if(isNaN(side)){
  console.log('Missing size');
} else {
  for ( i = 0; i < side; i++) {
    console.log('X'.repeat(side));
  }
}
