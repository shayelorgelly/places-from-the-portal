const { colorText } = require("./recolor")
module.exports.print = (text)=>{
    process.stdout.write(`${text}`);
}
module.exports.printColor = (text, color)=>{
    process.stdout.write(`${colorText(text, color)}`);
}
