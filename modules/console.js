const { colorText } = require("./recolor");
const fs = require("fs")
const readline = require("node:readline")
module.exports.print = (text)=>{//print regular text (same as console.log())
    // process.stdout.write(`${text}`);
    fs.writeSync(1, String(text))
}
module.exports.printColor = (text, color)=>{//print colored text to console
    // process.stdout.write(`${colorText(text, color)}`);
    fs.writeSync(1, String(colorText(text, color)));
}
module.exports.clear = ()=>{//use ansi code to clear console
    // process.stdout.write("\033c");
    fs.writeSync(1, String("\033c"));
}
//non async input function that doesnt use callbacks
module.exports.input = (msg)=>{//this function is quite complicated, but it does work
        fs.writeSync(1, String(msg));//print to stdout (process.stdout)(console.log)(print())
        let s = '', buf = Buffer.alloc(1);
        while(buf[0] - 10 && buf[0] - 13)//reads input from stdin until it encounters a newline (\n) or return (\r) and returns the input as a string.
          s += buf, fs.readSync(0, buf, 0, 1, 0);
        return s.slice(1);
}
