var express = require('express');
var router = express.Router();
var certificates = require('../controllers/certificate');

router.route('/certificates/:organizationID?')
    .get(certificates.apiGET)
    .post(certificates.apiPOST);
module.exports = router;
