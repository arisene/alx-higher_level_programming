#!/usr/bin/node
const { argv } = require('node:process');

const firstIndex = argv[2];

if (firstIndex === undefined) {
  console.log('No argument');
} else {
  console.log(`${firstIndex}`);
}
