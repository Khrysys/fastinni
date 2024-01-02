const HtmlWebpackPlugin = require('html-webpack-plugin');
const path = require('path');

module.exports = {
    entry: './static/main.jsx',
    mode: 'development',
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
                use: ['style-loader', 'css-loader', "sass-loader"]
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