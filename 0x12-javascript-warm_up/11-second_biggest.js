#!/usr/bin/node
const { argv } = require('node:process');

const numList = [];
if (isNaN(argv[2]) || argv.length <= 2) {
  console.log(0);
} else {
  for (let i = 2; i <= argv.length - 1; i++) {
    numList.push(argv[i]);
  }
  // console.log(numList.sort());
  const newList = numList.sort().reverse();
  console.log(newList[1]);
}
