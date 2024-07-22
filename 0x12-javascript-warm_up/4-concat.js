#!/usr/bin/node
const { argv } = require('node:process');

let firstIndex = argv[2];

if(argv.length <= 2){
    console.log('undefined is undefined');
}else if(argv.length === 3){
    console.log(`${firstIndex} is undefined`);
}else{
    console.log(`${firstIndex} is ${argv[3]}`);
}