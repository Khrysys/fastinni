const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const DotenvWebpackPlugin = require('dotenv-webpack');

module.exports = {
    entry: './html/main.js',
    mode: 'development',
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Fastinni', 
            favicon: "./static/favicon.ico"
        }),
        new CopyWebpackPlugin({
            patterns: [
                {'from': './static/img', 'to': '../html/img'}
            ]
        }),
        new DotenvWebpackPlugin({
            path: "./.env",
            safe: false
        })
    ],
    output: {
      filename: 'js/[name].js',
      path: path.resolve(__dirname, 'html'),
    },
    module: {
        rules: [
            {
                test: /\.css$/i,
                use: ['style-loader', 'css-loader']
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource'
            },
            {
                test: /\.(woff|woff2|eot|ttf|otf)$/i,
                type: 'asset/resource',
            },
        ]
    },
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    }
};