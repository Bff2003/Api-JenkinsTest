var express = require('express');
var app = express();
var assert = require('assert');
var request = require('request');

// get params of node run command
var args = process.argv.slice(2);

app.get('/helloWorld', function (req, res) {
    res.status(200).send('Hello World');
})

app.get('/json', function (req, res) {
    res.status(200).json({ message: 'Hello World' });
})

function test() {
    console.log('Inside test function');
    request('http://localhost:8081/helloWorld', function (error, response, body) {
        assert.equal(200, response.statusCode);
        assert.equal('Hello World', body);
    })

    request('http://localhost:8081/json', function (error, response, body) {
        assert.equal(200, response.statusCode);
        assert.equal('{"message":"Hello World"}', body);
    })

    console.log('Test completed');
}

var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)

   if (args[0] === 'test') {
        console.log('test mode');
        test();
        process.exit(0);
   }
})
