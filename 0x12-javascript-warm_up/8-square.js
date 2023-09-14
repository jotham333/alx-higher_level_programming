#!/usr/bin/node
const arg = process.argv[2];
const intValue = parseInt(arg);

if (isNaN(intValue) || arg === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < intValue; i++) {
    console.log('X'.repeat(intValue));
  }
}
