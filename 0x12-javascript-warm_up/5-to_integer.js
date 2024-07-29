#!/usr/bin/node
const { argv } = require('node:process');

const firstIndex = parseInt(argv[2]);
if (isNaN(firstIndex)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${firstIndex}`);
}
