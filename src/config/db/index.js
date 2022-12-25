const mongoose = require('mongoose');

async function connect() {
    try {
        await mongoose.connect('mongodb://192.168.20.156:27017/Video');
        console.log('Connect successfully');
    } catch (error) {
        console.log('Connect fail !!');
    }
}

module.exports = { connect };
