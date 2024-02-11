const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require("mini-css-extract-plugin");
const path = require('path');

const devMode = process.env.NODE_ENV != 'production';

module.exports = {
    entry: {
        index: './static/main.jsx',
        admin: './static/admin.jsx'
    },

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
            filename: 'index.html',
            favicon: "./static/favicon.ico",
            chunks: ['index', 'vendor']
        }),
        new HtmlWebpackPlugin({
            title: 'Fastinni Admin',
            filename: 'admin/index.html',
            favicon: './static/favicon.ico',
            chunks: ['admin', 'vendor']
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
                        ],
                        env: {
                            "production": {
                                "presets": ["react-optimize"]
                            }
                        }
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