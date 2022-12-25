const path = require('path');
const express = require('express');
const morgan = require('morgan');
const { engine } = require('express-handlebars');
const methodOverride = require('method-override');

const route = require('./routes');
const db = require('./config/db');

const app = express();
const port = 3000;

// Connect to DB
db.connect();

app.use(express.json());

app.use(express.static(path.join(__dirname, 'public/')));
app.use(express.static('/mlcv/Databases/HCM_AIC22/'));


app.use(
    express.urlencoded({
        extended: true,
    }),
);
app.use(express.json());

// HTTP logger
app.use(morgan('combined'));

app.use(methodOverride('_method'));

// Template engine
app.engine(
    'handlebars',
    engine({
        extname: '.handlebars',
        helpers: {
            sum: (a, b) => a + b,
        },
    }),
);

app.set('view engine', 'handlebars');
app.set('views', path.join(__dirname, 'resources/views'));

// route init
route(app);
// app.get('/', (req, res) => res.render("home"))

app.listen(port, () => console.log(`App listening on port ${port}`));
