var CertificateResponse = require("../BO/certificateResponseObj.js");
//var sdg = require("./sdgs.js")
//var connection = require("../db_connection")
var pool = require("../db_connection")

exports.apiGET = async function(req, res) {
    var certificates = []
        var sql_resp = await pool.query('select * from certificates where organizationID = ?', req.params.organizationID)

        for (i = 0; i < sql_resp.length; i++) {
            var certificateID = sql_resp[i].certificateID
            var sdgs = [];
            var sdgTargets = [];
            sql_resp2 = await pool.query('select sdgID from certificate_sdg where certificateID = ?', certificateID)
            for(j = 0; j < sql_resp2.length; j++) {
                sdgs.push(sql_resp2[j].sdgID)
                console.log('sdgs:', sdgs)
                console.log('sql_response2:', sql_resp2)
            }

            sql_resp3 = await pool.query('select sdgTargetID from certificate_sdgTarget where certificateID = ?', certificateID)
            for(k = 0; k < sql_resp3.length; k++) {
                sdgTargets.push(sql_resp3[k].sdgTargetID)
                console.log('sdgTargets:', sdgs)
                console.log('sql_response3:', sql_resp3)
            }


            var certificateResponse = new CertificateResponse(sql_resp[i], sdgs, sdgTargets)
            certificates.push(certificateResponse)
        }
        res.json(certificates);


};


/*
pooling version

exports.apiGET = async function(req, res) {
    var certificates = []
    await pool.getConnection(function(err, connection) {
        connection.query('select * from certificates where organizationID = ?', req.params.organizationID, (err, sql_resp) => {
            connection.release()
            if (err) res.json({msg: err});

            else {

                for (i = 0; i < sql_resp.length; i++) {
                    var certificateID = sql_resp[i].certificateID
                    var sdgs;
                    sdgs = sdg.getSdgs(certificateID);
                    var sdgTargets = sdg.getSdgTargets(certificateID)
                    var certificateResponse = new CertificateResponse(sql_resp[i], sdgs, sdgTargets)
                    certificates.push(certificateResponse)
                }
                res.json(certificates);
                console.log('Fetched certificates successfully', certificates);
            }
        })
    })

};

 */

/*
Done all wierd stuff due to async and callbacks
exports.apiGET = function(req, res) {
    var certificates = []
    var query = connection.query('select * from certificates where organizationID = ?', req.params.organizationID)
    query
        .on('result', function(sql_resp) {
            processRow(sql_resp, function() {
                    sql_resp.forEach(
                        certificate => {

                            var certificateID = certificate.certificateID
                            var sdgs = []
                            var sdgTargets = []
                            var query2 = connection.query('select sdgID from certificate_sdg where certificateID = ?', certificateID)
                            query2.on('result', function (sql_resp2) {
                                processRow(sql_resp2, function(){
                                    sql_resp2.forEach(
                                    sdg => {
                                        sdgs.push(sdg.sdgID)
                                        console.log('sdgs:', sdgs)
                                    }
                                )});

                                certificateResponse.sdgs = sdgs
                                console.log('sql_response2:', sql_resp2)
                            })
                            var query3 = connection.query('select sdgTargetID from certificate_sdgTarget where certificateID = ?', certificateID)
                            query3.on('result', (sql_resp3) => {
                                sdgTargets.push(sql_resp3)
                                console.log('sql_response3:', sql_resp3)
                            })
                            var certificateResponse = new CertificateResponse(certificate, sdgs, sdgTargets)
                            certificates.push(certificateResponse)
                        }
                    )
                }
            );
})
        .on('end',function() {    res.json(certificates);
            console.log('Fetched certificates successfully', certificates);})

};


*/

exports.apiPOST = async function(req, res) {
    await pool.query('INSERT INTO certificates SET ?', req.body.basicDetails, (err, sql_resp) => {
        var certificateId = sql_resp.insertId

        req.body.sdgs.forEach(sdg => pool.query('INSERT INTO certificate_sdg (certificateID, sdgID) values (?,?)',[certificateId,sdg]))
        req.body.sdgTargets.forEach(sdgTarget => pool.query('INSERT INTO certificate_sdgTarget (certificateID, sdgTargetID) values (?,?)',[certificateId,sdgTarget]))

        if(err)  res.json({msg: err});
        else{
            res.json({msg:"Added Certificate successfully with ID:"+ sql_resp.insertId});}

    });
};

exports.apiPUT = function(req, res) {
    pool.query('UPDATE certificates SET ? WHERE certificateID = ?', [req.body.basicDetails,req.body.certificateID], (err, sql_resp) => {
        if(err) throw err;
        else{
            res.json({msg:"Updated Certificate successfully"});}

    });
};
