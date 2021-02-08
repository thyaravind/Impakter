var connection = require("../db_connection")



exports.apiGET = function(req, res) {
    connection.query('select * from certificates where organizationID = ?', req.params.organizationID, (err, sql_resp) => {

        sql_resp.forEach(certificate => {
            var certificateID = certificate.certificateID;
            sdgs = connection.query('select sdgID from certificate_sdg where certificateID = ?',certificateID)
        })

        if(err) throw err;
        else{
            res.json(sql_resp,sdgs);}

        console.log('Fetched certificates successfully', sql_resp);
    });


};

exports.apiPOST = function(req, res) {
    connection.query('INSERT INTO certificates SET ?', req.body.payload, (err, sql_resp) => {
        var certificateId = sql_resp.insertId

        req.body.sdgs.forEach(sdg => connection.query('INSERT INTO certificate_sdg (certificateID, sdgID) values (?,?)',[certificateId,sdg]))

        if(err)  res.json({msg: err});
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
