#!/usr/bin/node
const und = 'undefined';
if (!process.argv[2]) {
  process.argv[2] = und;
}
if (!process.argv[3]) {
  process.argv[3] = und;
}
console.log(process.argv[2] + ' is ' + process.argv[3]);
