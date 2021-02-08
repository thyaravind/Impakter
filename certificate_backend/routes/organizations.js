var express = require('express');
var router = express.Router();
var organization = require('../controllers/organization');

router.route('/organizations/:organizationID?')
    .get(organization.apiGetOne)
    .get(organization.apiGetAll)
    .post(organization.apiPOST);
module.exports = router;
