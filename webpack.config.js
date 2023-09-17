const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CopyWebpackPlugin = require('copy-webpack-plugin');
const DotenvWebpackPlugin = require('dotenv-webpack');

module.exports = {
    entry: './src/index.js',
    mode: 'development',
    plugins: [
        new HtmlWebpackPlugin({
            title: 'Fastinni'
        }),
        new CopyWebpackPlugin({
            patterns: [
                {'from': './src/copy', 'to': './'}
            ]
        }),
        new DotenvWebpackPlugin({
            path: "./.env",
            safe: false
        })
    ],
    output: {
      filename: 'js/[name].js',
      path: path.resolve(__dirname, 'fastinni/pages'),
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
    }
};