#!/usr/bin/node

const { argv } = require('node:process');

const firstInt = Number(argv[2]);
const secondInt = Number(argv[3]);

if (isNaN(firstInt) || isNaN(secondInt)) {
  console.log('NaN');
} else {
  add(firstInt, secondInt);
}

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}
