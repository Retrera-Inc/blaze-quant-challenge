const express = require('express');
const { storePortfolio } = require('../controllers');

const router = express.Router();
router.route('/holdings').post(storePortfolio);

module.exports =  router;
