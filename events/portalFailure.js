    const { fakeTypingPrintTimerColor, waitSync } = require("../modules/timer")//| places-from-the-portal\modules\timer.js
    const { print, printColor } = require("../modules/console") //ctrl click on the function to view source
    const { config } = require("../configuration/config")
    module.exports.types = [
        "antimatterGenerationFailure", //antimatter generation failure
        "cooldown"
    ];
    module.exports.portalFailure = (type)=>{
        let red = [255,25,25]//rgb color code
        if (type == "cooldown"){
            fakeTypingPrintTimerColor("Portal has failed to start", config.defaultTextSpeed, red)
            fakeTypingPrintTimerColor("...", 300, red)
            print("\n")//newline
            diagnosticsReport("Portal mainframe controller is currently cooling down\nPlease wait for the system to complete this process\n")
        }
        if (type == "antimatterGenerationFailure"){
            fakeTypingPrintTimerColor("Antimatter Generator has failed to start", config.defaultTextSpeed, red)
        }
    }
const diagnosticsReport = (information)=>{
    fakeTypingPrintTimerColor("Diagnostics report generated", config.defaultTextSpeed, [0, 135, 255]);
    waitSync(500)
    fakeTypingPrintTimerColor(("\n") + information, config.defaultTextSpeed * 1.5, [70,70,70])
    return true
}