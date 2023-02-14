DESCRIPTION - Server that provides a json of quotes related to time. Written in Python and using Flask framework. 

REQUESTING DATA: 
1) GET http://127.0.0.1:5000/quotes.json
2) The response will be a json of quotes/authors


RETRIEVING DATA: Example in Javascript

const endpoint = 'http://127.0.0.1:5000/quotes.json';

import('node-fetch').then(({default: fetch}) => 
{
    fetch(endpoint)
    .then(response => {
    if (response.ok) 
    {
        return response.json();
    }
    else 
    {
        throw new Error(`Error`);
    }
    })
    .then(data => 
    {
        const quotes = data.quotes;
        const randomIndex = Math.floor(Math.random() * quotes.length);
        const {quote, author} = quotes[randomIndex];
        console.log(`"${quote}" - ${author}`);
    })
    .catch(error => 
    {
      console.error(error.message);
    });
});

1) Use node-fetch to fetch the data
2) To install, run npm install node-fetch in terminal

UML DIAGRAM:
![UML Sequence](https://user-images.githubusercontent.com/110798437/218688492-eb60d617-197e-4b04-a3a7-8cdbccd58a9d.png)

