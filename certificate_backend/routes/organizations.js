var express = require('express');
var router = express.Router();
var certificates = require('../controllers/organization');

router.route('/organizations')
    .get(certificates.apiGET)
    .post(certificates.apiPOST);
module.exports = router;
