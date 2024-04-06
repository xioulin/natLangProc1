const deadPrez= ['washington','lincoln','trump','nixon','reagan'];

// for (let i=0; i<deadPrez.length;i++){
//     console.log(deadPrez[i])
// }

var HTMLParser=require('node-html-parser');
var root= HTMLParser.parse("<div id='div1'>hello</div>")


// const path=require('path')
// const fs = require('fs');
// const directoryPath= path.join(__dirname,'prez_img')
// fs.readdir(directoryPath, function (err, files) {
//     //handling error
//     if (err) {
//         return console.log('Unable to scan directory: ' + err);
//     }
//     //listing all files using forEach
//     files.forEach(function (file) {
//         // Do whatever you want to do with the file
//         console.log(file)
//     });
// });
//
//

