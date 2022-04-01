#!/usr/bin/node
const { argv } = require('process');
const n = parseInt(argv[2]);
if (!n) {
  console.log('Missing size');
} else {
  for (let i = 0; i < n; i++) {
    let sqr = 'X';
    console.log(sqr.repeat(n));
  }
}
