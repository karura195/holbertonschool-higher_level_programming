#!/usr/bin/node
const Squares = require('./5-square');
class Square extends Squares {
  charPrint (c) {
    const x = !c ? 'X' : c;
    for (let i = 0; i < this.height; i++) {
      console.log(x.repeat(this.width));
    }
  }
}

module.exports = Square;
