const http = require('http');
const url = require('url');

const server = http.createServer(function(req, res) {

    const q = url.parse(req.url, true).query;

    const num1 = parseInt(q.num1);
    const num2 = parseInt(q.num2);

    res.writeHead(200, {'Content-Type': 'text/html'});

    if (!isNaN(num1) && !isNaN(num2)) {

        let largest;

        if (num1 > num2) {
            largest = num1;
        } 
        else if (num2 > num1) {
            largest = num2;
        } 
        else {
            largest = "Both numbers are equal";
        }

        res.write("<h1>Largest Number Result</h1>");
        res.write("<p>Number 1: " + num1 + "</p>");
        res.write("<p>Number 2: " + num2 + "</p>");
        res.write("<h2>Largest: " + largest + "</h2>");
    }
    else {
        res.write("<h1>Please provide numbers in URL</h1>");
        res.write("<p>Example: http://localhost:3000/?num1=10&num2=20</p>");
    }

    res.end();
});

server.listen(3000);
console.log("Server running at http://localhost:3000/");