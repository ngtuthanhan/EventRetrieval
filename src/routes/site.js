const express = require('express');
const router = express.Router();

const siteController = require('../app/controllers/SiteController');

// newController.index
router.get('/search', siteController.search);
router.post('/search', siteController.getData);
router.get('/', siteController.index);
router.post('/', siteController.getData);
router.get('/Detail/:idframe', siteController.showDetail);
router.get('/KNN/:idframe', siteController.showKNN);


module.exports = router;
