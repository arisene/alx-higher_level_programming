#!/usr/bin/node

const { argv } = require('node:process');

const number = Number(argv[2]);

function factorial (number) {
  if (number < 0) {
    console.log('Error! Factorial for negative number does not exist.');
  } else if (number === 0 || isNaN(number)) {
    console.log(1);
  } else {
    let fact = 1;
    for (let i = 1; i <= number; i++) {
      fact *= i;
    }
    console.log(`${fact}`);
  }
}

factorial(number);
