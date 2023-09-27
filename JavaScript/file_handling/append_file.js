const fs = require('fs');

fs.appendFile('sample.txt', 'Appending Content', (error) => {
	if (error) {
		console.log(error);
	} else {
		console.log('Completed');
	}})
