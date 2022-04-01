#!/usr/bin/node
const { argv } = require('process');
const n = parseInt(argv[2]);
function factorial (n) {
  if (!n) {
    return (1);
  }
  if (n !== 0) {
    return (n * factorial(n - 1));
  }
}
console.log(factorial(n));
