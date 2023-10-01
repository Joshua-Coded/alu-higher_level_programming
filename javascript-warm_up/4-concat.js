#!/usr/bin/node
if (process.argv[2]) {
  console.log(process.argv[2] + ' ' + 'is' + ' ' + process.argv[3]);
} else if (process.argv[1]) {
  console.log(process.argv[1]  + ' is ' + ' ' + undefined);
} else {
  console.log(process.argv[1] + 'is' + ' ' + undefined)
}
