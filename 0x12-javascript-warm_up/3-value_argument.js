#!/usr/bin/node
const { argv } = require('node:process');

let firstIndex = argv[2];

if(argv.length <= 2){
    console.log('No argument');
}else{
    console.log(`${firstIndex}`);
}