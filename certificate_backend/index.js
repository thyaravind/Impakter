var express = require('express');
var mongoose = require('mongoose');
var bodyparser = require('body-parser');
var cors = require('cors');
var path = require('path');

var app = express();


const port = 3000;
const route = require('./routes');


//conecting to MongoDB
mongoose.connect('mongodb://localhost:27017/orgs')
mongoose.connection.on('connected',()=> {
    console.log('connected to MongoDB');
})
mongoose.connection.on('error',(err)=> {
    if(err){
        console.log('Error connecting to DB');
    }
    
})


app.use(bodyparser.json());


app.use('/api',route)

app.use(cors());

app.use(express.static(path.join(__dirname,'public')));


app.listen(port,() => {console.log('App is up and running at port:'+port)})