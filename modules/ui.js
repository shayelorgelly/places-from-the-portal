const { colorText, colorLog, colorBG } = require("./recolor.js")
module.exports = {
    getTerminalSize: ()=>{
        return [process.stdout.rows, process.stdout.columns]
    },
    checkTerminalSize: (rows, columns)=>{//checks if the terminal size is within the rows/colums
        let currentSize = module.exports.getTerminalSize()
        let minSize = [rows, columns]
        if(minSize[0] > currentSize[0] || minSize[1] > currentSize){
            return false// terminal is not big enough to meet rows/columns requirement
        }
        return true
    },
    shapes: {
        "line": (color)=>{
            return colorBG(" ".repeat(module.exports.getTerminalSize()[1]), color)
        }
        
    }
}