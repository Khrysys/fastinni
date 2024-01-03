const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require('path');

const devMode = process.env.NODE_ENV != 'production';
console.log(process.env.NODE_ENV)
console.log(devMode)

module.exports = {
    entry: './static/main.jsx',
    mode: devMode ? "development" : "production",
    stats: {
        errorDetails: true
    },
    
    output: {
        filename: 'js/[name].js',
        path: path.resolve(__dirname, 'html'),
    },

    resolve: {
        extensions: ['.js', '.jsx', '.json', '.wasm']
    },

    plugins: [
        new HtmlWebpackPlugin({
            title: 'Fastinni', 
            favicon: "./static/favicon.ico",
        }),
        new MiniCssExtractPlugin({})
    ],

    module: {
        rules: [
            {
                test: /\.jsx$/i,
                exclude: '/node-modules/',
                use: {
                    loader: 'babel-loader',
                    options: {
                        presets: [
                            [
                                "@babel/preset-react", 
                                {
                                    "runtime": "automatic"
                                }
                            ],
                            [
                                "@babel/preset-env",
                                {
                                    "targets": [
                                        "> 0.25%, not dead"
                                    ]
                                }
                            ]
                        ],
                        plugins: [
                            [
                                "macros",
                                {}
                            ]
                        ]
                    }
                }
            },
            {
                test: /\.scss$/i,
                use: [devMode ? "style-loader" : MiniCssExtractPlugin.loader, 'css-loader', "sass-loader"]
            },
            {
                test: /\.(png|svg|jpg|jpeg|gif)$/i,
                type: 'asset/resource'
            },
        ]
    },
    optimization: {
        splitChunks: {
            chunks: 'all'
        }
    }
}