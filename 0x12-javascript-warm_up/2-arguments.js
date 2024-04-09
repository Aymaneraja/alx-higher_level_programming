#!/usr/bin/node
if (process.argv.lenght === 2){
	console.log('No arguments');
}else if (process.argv.lenght === 3){
	console.log('Argument found');
}else{
	console.log('Arguments found');
}
