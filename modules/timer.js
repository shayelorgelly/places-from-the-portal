const {printColor} = require("./console.js")
const { getRandomInt } = require("./randomer.js")
module.exports.waitSync = (ms)=>{
    var start = Date.now(),
        now = start;
    while (now - start < ms) {
      now = Date.now();
    }
}
module.exports.loopPrintOnTimer = (data, i, milliseconds, nonewline)=>{
    let _i = 0
    while(_i <= i){//loop <i> times
        process.stdout.write(data);
        this.waitSync(milliseconds);//"this" means this scripts module exports 
        _i++;
    }
    if(!nonewline){
        process.stdout.write("\n")
    }
}
module.exports.fakeTypingPrintTimerColor = (data, ms, rgbarray)=>{
    let _i = 0;
    while (_i <= data.length){
        this.waitSync(ms)
        printColor(data.charAt(_i), rgbarray)
        _i++
    }
}
module.exports.fakeTypingPrintTimerRandomColor = (data, ms, rgbarray)=>{
    let _i = 0;
    while (_i <= data.length){
        this.waitSync(ms)
        printColor(data.charAt(_i), rgbarray)
        _i++
    }
}