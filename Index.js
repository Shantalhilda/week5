const express = require('express');
const app = express();
const port = 5000;

app.get('/greetings', (request, response) => {
    return response.send({msg: "Hello Steve"});
});

// List of friends 
let friends = [{"id": 1, "name":'Steve'},
     {"id": 2, "name":'Kaylor'}, 
     {"id": 3, "name":'Adrian'}, 
     {"id":4, "name":'Jordan'}, 
     {"id": 5, "name":'Marvin'}];
app.get('/list-of-friends', (request, response) => {
    return response.send(friends);

app.get('/list-of-friends-by-id/:id', )

});



app.listen(port, () => {

    console.log(`Example app listening at http://localhost:${port}`);
});