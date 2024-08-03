#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
  YOUR CODE HERE
  */
Object.keys(myObject).forEach((item) => {
  if (myObject[item] === 12) {
    myObject[item] = 89;
  }
});
console.log(myObject);
