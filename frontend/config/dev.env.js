'use strict'
const merge = require('webpack-merge')
const prodEnv = require('./prod.env')

module.exports = merge(prodEnv, {
    NODE_ENV: '"development"',

    VUE_MOGU_WEB: '"http://localhost:9527"',
    PICTURE_API: '"http://localhost:8602"',
    WEB_API: '"http://localhost:5000"',
    // WEB_API: '"http://192.168.43.68:5000"',
    ELASTICSEARCH: '"http://localhost:8605"',

})