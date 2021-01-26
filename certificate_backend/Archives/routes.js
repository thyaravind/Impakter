const express = require('express');
const router = express.Router();
const Organization = require('../models/organizations')
const mysql = require('mysql');

const connection = mysql.createConnection({
    host: 'localhost',
    user: 'root',
    password: 'hakunaMATATA02@',
    database: 'impakter_certificates',
    port: 3306
});
connection.connect((err) => {
    if (err) throw err;
    console.log('MySQL Connected!');
});



router.get('/orgs',(req,res,next)=>{

    Organization.find(function(err,organizations){
        res.json(organizations);
    })
});

router.post('/orgs/create',(req,res,next)=>{

    connection.query('INSERT INTO certificateOrganizations SET ?', req.body, (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Added Org successfully"});}

        console.log('Added the organization with insert ID:', sql_resp.insertId);
    });

    /* using MongoDB
    let newOrg = new Organization({
        organizationName: req.body.name,
        country: req.body.country
    });
    newOrg.save((err,org)=> {
        if(err){
            res.json({msg:"Failed to add Org"});

        }
        else{
            res.json({msg:"Added Org successfully"});

        }

    }) */
});


//Using route parameters
router.delete('/orgs/:id',(req,res,next)=>{
    Organization.remove({_id: req.params.id},function(err, result){
        if(err){
            res.json(err);
        }
        else{
            res.json(result);
        }

    })
});


//Using route parameters
router.get('/certificates/:id',(req,res,next)=>{
    Organization.remove({_id: req.params.id},function(err, result){
        if(err){
            res.json(err);
        }
        else{
            res.json(result);
        }

    })
});

module.exports = router;
