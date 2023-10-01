#!/usr/bin/node
function add (a, b) {
  const d = a + b;
  console.log(d);
}

add(Number(process.argv[2]), Number(process.argv[3]));
