var connection = require("../db_connection")



exports.apiGetAll = function(req, res) {
    connection.query('SELECT * from certificateOrganizations', (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Orgs fetched successfully",organizationDetails: sql_resp});}
    });


};

exports.apiGetOne = function(req, res) {
    connection.query('SELECT * from certificateOrganizations where organizationID = ?',req.params.organizationID, (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Org fetched successfully",organizationDetails: sql_resp});}
    });


};

exports.apiPOST = function(req, res) {
    connection.query('INSERT INTO certificateOrganizations SET ?', req.body, (err, sql_resp) => {
        if(err) throw err;
        else{
            var message = 'Added the organization with insert ID:' + sql_resp.insertId;
            res.json({msg:message});}

        console.log(message);
    });
};
