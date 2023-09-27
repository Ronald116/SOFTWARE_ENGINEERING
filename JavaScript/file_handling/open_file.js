const fs = require('fs');

fs.open('sample.txt', 'w', (error, file) => {
	if (error) {
		console.log(error);
	} else {
		console.log(file);
	}})
