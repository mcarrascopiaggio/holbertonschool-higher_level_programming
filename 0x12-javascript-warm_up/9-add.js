#!/usr/bin/node
const { argv } = require('process');
const first = parseInt(argv[2]);
const second = parseInt(argv[3]);

function add (a, b) {
  const c = a + b;
  console.log(c);
}
add(first, second);
