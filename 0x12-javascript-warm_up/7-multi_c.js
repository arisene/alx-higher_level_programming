#!/usr/bin/node

const { argv } = require('node:process');
const occNum = argv[2];
if (isNaN(occNum)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 1; i <= occNum; i++) {
    console.log('C is fun');
  }
}
