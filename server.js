require('dotenv').config();
const express = require('express');
const path = require('path');
const session = require('express-session');
const flash = require('connect-flash');
const fileUpload = require('express-fileupload');

const app = express();

// Session
app.use(session({
    secret: process.env.SESSION_SECRET || 'change_this',
    resave: false,
    saveUninitialized: false
}));
app.use(flash());

// View Engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Static files
app.use(express.static(path.join(__dirname, 'public')));
app.use('/static', express.static(path.join(__dirname, 'public/static')));

// Middleware
app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(fileUpload());

// User model mock (until DB setup)
const { mockCurrentUser } = require('./models/user');
app.use((req, res, next) => {
    res.locals.current_user = mockCurrentUser;  // Replace with real session-based logic
    next();
});

// Routes
const authRoutes = require('./routes/auth');
const settingsRoutes = require('./routes/settings');
const mediaRoutes = require('./routes/media');
const homeRoutes = require('./routes/home');

app.use('/', homeRoutes);
app.use('/auth', authRoutes);
app.use('/settings', settingsRoutes);
app.use('/media', mediaRoutes);

// Start Server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
    console.log(`🚀 Server running at http://localhost:${PORT}`);
});
