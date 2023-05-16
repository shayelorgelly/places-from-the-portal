module.exports.colorText = (message,rgbarray)=>{//recolor v2
    return(`\x1b[38;2;${rgbarray.join(";")}m${message}\x1b[0m`)//will not work if truecolor isnt supported
};
module.exports.colorLog = (message,rgbarray)=>{
    console.log(`\x1b[38;2;${rgbarray.join(";")}m${message}\x1b[0m`)
    return true
}