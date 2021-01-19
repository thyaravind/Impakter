const express = require('express');
const router = express.Router();
const Organization = require('./models/organizations')

router.get('/orgs',(req,res,next)=>{

    Organization.find(function(err,organizations){
        res.json(organizations);
    })
});

router.post('/orgs/create',(req,res,next)=>{
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

    })
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


module.exports = router;