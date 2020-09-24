// const mongoose = require('mongoose');
// const Schema = mongoose.Schema;

// const BookSchema = new Schema({
//     title: String,
//     pages: Number,
// });

// const AuthorSchema = new Schema({
//     name: String,
//     weight: Number,
//     book:[BookSchema],
// });

// const Author = mongoose.model('author',AuthorSchema);

// module.exports = Author;y
const mongoose = require('mongoose');
const Schema = mongoose.Schema;

// Create a Schema and a Model

const BookSchema = new Schema({
    title: String,
    pages: Number
});

const AuthorSchema = new Schema({
    name: String,
    books: [BookSchema]
});

const Author = mongoose.model('author', AuthorSchema);

module.exports = Author;