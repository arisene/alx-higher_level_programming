#!/usr/bin/node
const { argv } = require('node:process');

// last index
let lastIndex = argv.length - 1

if (lastIndex === 1) {
    console.log('No argument')
}else if(lastIndex === 2){
    console.log('Argument found')
}else{
    console.log('Arguments found')
}
