#!/usr/bin/node

const { argv } = require('node:process');

const sizeSq = argv[2];
if (isNaN(sizeSq)) {
  console.log('Missing size');
} else {
  for (let i = 1; i <= sizeSq; i++) {
    let line = '';
    for (let j = 1; j <= sizeSq; j++) {
      line += 'X';
    }
    console.log(line);
  }
}
