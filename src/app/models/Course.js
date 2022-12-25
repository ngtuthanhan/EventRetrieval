const mongoose = require('mongoose');
const slug = require('mongoose-slug-generator');
const Schema = mongoose.Schema;
const mongooseDelete = require('mongoose-delete');

const Course = new Schema(
    {
        VideoID: { type: String},
        KeyFrame: { type: String },
        Batch: { type: String },
        TrueFrame: {type: Number },
        PositionFrame: {type: Number },
        IDFrame: {type: String }
    },
    {
        timestamps: true,
    },
);

// Add plugin
mongoose.plugin(slug);
Course.plugin(mongooseDelete, {
    overrideMethods: 'all',
    deletedAt: true,
});

module.exports = mongoose.model('Course', Course, 'KeyFrameBatch3V4');
