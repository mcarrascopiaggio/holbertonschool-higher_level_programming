#!/usr/bin/node
let myvar = 'is';
if (process.argv.length === 4) {
  console.log(process.argv[2] + ' ' + myvar + ' ' + process.argv[3]);
} else if (process.argv === 3){
  console.log(process.argv[2] + ' ' + myvar + ' ' + 'undefined');
} else {
  console.log(process.argv[2]);
}
