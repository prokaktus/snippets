'use strict';

var path = require('path');
var extract = require('extract-text-webpack-plugin');

const PATHS = {
    app: path.join(__dirname, 'index.js'),
    build: path.join(__dirname, 'build')
}

var config = {
    entry: PATHS.app,
    output: {
        path: PATHS.build,
        filename: 'bundle.js'
    },
    module: {
        loaders: [
            { 
                test: /\.css$/,
                loader: extract.extract("style-loader", "css-loader")
            },
            { 
                test: /\.jsx?$/,
                loader: 'babel',
                exclude: /(node_modules|bower_components)/,
                query: {
                    presets: ['es2015']
                }
            }
        ]
    },
    devtool: 'source-map',
    plugins: [
        new extract("styles.css")
    ]
}

module.exports = config;

