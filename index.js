const express = require('express');
//service import
const my_business_logic = require('./service/my_business_logic');

const app = express();
const port = 4000;
app.use(express.json());

//get
app.get('/',(request, response) => {
    response.send('hello shantal');
})
//greetings
app.get('/greetings', (request, response) => {
    return response.send({msg: 'Hello shantal!'});
});

//list of friends
let_friends = [
    {"id":1,"name":"tom"},
    {"id":2,"name":"peter"},
    {"id":3,"name":"jane"},
    {"id":4,"name":"james"},
    {"id":5,"name":"shan"}];

app.get('/list-of-friends', (request,response)=>{

    return response.status(200).send(my_business_logic.getStudentById(request));

});

app.get('/list-of-friends-by-id/:id', (request,response)=>{
    console.log('loging request params', request.params);

    return response.send("sending nothing back");
});

//POST
app.post('sign-up', (request, response) => {
    console.log('loging request body', request.body);

    return response.status(200).send("heeey we are using a post method");

});


//delete
app.delete('/delete_student', (request, response) => {
    console.log('loging request body', request.body);

    return response.status(200).send("heeey we are using a post method");

});

//





app.listen(port, () => {
console.log(`Example app listening at http://localhost:${port}`);
});