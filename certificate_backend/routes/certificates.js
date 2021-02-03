var express = require('express');
var router = express.Router();
var certificate = require('../controllers/certificate');

router.route('/certificates/:organizationID?')
    .get(certificate.apiGET)
    .post(certificate.apiPOST)
    .put(certificate.apiPUT);
module.exports = router;
