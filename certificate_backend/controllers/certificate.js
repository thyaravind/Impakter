var connection = require("../db_connection")



exports.apiGET = function(req, res) {
    connection.query('select * from certificates where organizationID = ?', req.params.organizationID, (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json(sql_resp);}

        console.log('Fetched certificates successfully', sql_resp);
    });


};

exports.apiPOST = function(req, res) {
    connection.query('INSERT INTO certificates SET ?', req.body.payload, (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Added Certificate successfully with ID:"+ sql_resp.insertId});}

    });
};

exports.apiPUT = function(req, res) {
    connection.query('UPDATE certificates SET ? WHERE certificateID = ?', [req.body.payload,req.body.certificateID], (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Updated Certificate successfully"});}

    });
};
