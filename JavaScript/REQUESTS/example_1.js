const request = require('request');

request('https://google.com', (error, response, body) => {
	console.log('error:', error);
	console.log('status:', response && response.statusCode);
	console.log('body:', body);
})
