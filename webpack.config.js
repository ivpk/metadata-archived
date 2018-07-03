module.exports = {
  entry: './ui/index.js',
  output: {
    path: __dirname + '/assets',
    filename: 'inven.bundle.js',
    publicPath: '/static/',
  },
  module: {
    rules: [
      {test: /\.css$/, use: [
        {loader: "style-loader"},
        {loader: "css-loader"},
      ]},
      {test: /\.(eot|svg|ttf|woff|woff2)$/, use: [
        {loader: 'file-loader'}
      ]}
    ]
  },
  devtool: 'eval',
};
