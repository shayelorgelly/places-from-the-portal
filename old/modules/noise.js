const {spawn, exec} = require("child_process");
const path = require("path");
module.exports.playSound = (epath)=>{
    exec(`powershell -c (New-Object Media.SoundPlayer '${path.resolve(epath)}').PlaySync();`);
}