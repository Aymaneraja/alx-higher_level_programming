#!/usr/bin/node
/* prints the first argument */
if (process.argv[2] === undefined) {
	console.log('No argument');
} else {
	console.log(process.argv[2]);
}
