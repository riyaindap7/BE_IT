const express = require('express');
const router = express.Router();
const { createUser, getUsers } = require('../controllers/UserController');

router.post('/', createUser); // POST /api/users
router.get('/', getUsers);    // GET /api/users

module.exports = router;
